// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include "DataFormats/Candidate/interface/Candidate.h"



//******************************************************************************
//                           Class declaration
//******************************************************************************

class FilterSample2GenMu : public edm::EDFilter
{
public:
  explicit FilterSample2GenMu(const edm::ParameterSet&);
  ~FilterSample2GenMu();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  virtual void beginJob() ;
  virtual bool filter(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;

  virtual void beginRun(edm::Run const&, edm::EventSetup const&);
  virtual void endRun(edm::Run const&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

  //****************************************************************************
  //          RECO LEVEL VARIABLES, BRANCHES, COUNTERS AND SELECTORS
  //****************************************************************************

  // Labels to access
  edm::EDGetTokenT<reco::GenParticleCollection > m_muons;
  edm::EDGetTokenT<reco::GenParticleCollection > m_candidates;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
FilterSample2GenMu::FilterSample2GenMu(const edm::ParameterSet& iConfig)
{
  m_muons           = consumes<reco::GenParticleCollection >(edm::InputTag("muons"));
  m_candidates      = consumes<reco::GenParticleCollection >(edm::InputTag("candidates"));
}


FilterSample2GenMu::~FilterSample2GenMu()
{
}

//
// member functions
//

// ------------ method called for each event  ------------
bool
FilterSample2GenMu::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;

  edm::Handle<reco::GenParticleCollection > muons;
  edm::Handle<reco::GenParticleCollection > candidates;
  iEvent.getByToken(m_muons, muons);
  iEvent.getByToken(m_candidates, candidates);
  //const reco::GenParticleCollection& muonC = *muons.product();
  const reco::GenParticleCollection& candidateC = *candidates.product();

  
  double muon_eta[5] = {0, 0, 0, 0, 0};
  double muon_phi[5] = {0, 0, 0, 0, 0};

  
  int mu1_index;
  int mu2_index;
  int check;
  double eta1;
  

  //Pick out muons (Id=+/- 13) that are final state muons (status=1) in the endcap system (1.2<|eta|<2.4).
  //Store their eta and phis into a local array to calculate dR in the next step.
  int j=0;
  for (std::size_t i=0 ; i<candidateC.size() ; i++) {
    if ((candidateC[i].pdgId() == 13) or (candidateC[i].pdgId() == -13) and (candidateC[i].status() == 1) and ((1.2 <= abs(candidateC[i].eta())) and (abs(candidateC[i].eta()) <= 2.4)) and (j<4)) {
      muon_eta[j] = candidateC[i].eta();
      muon_phi[j] = candidateC[i].phi();
      j++;
    }
  }


  //If four muons, check for two unique muon pairs, each pair with dR<0.5 that pass through different endcaps.
  if ((muon_eta[3] != 0) and (muon_eta[4]==0)) {

    for (int i=0 ; i<4 ; i++) {
      for (int j=0 ; j<4 ; j++) {

        if ((j!= i) and ((muon_eta[i] * muon_eta[j])) > 0) {
	    if (reco::deltaR(muon_eta[i], muon_phi[i], muon_eta[j], muon_phi[j]) < 0.5) {
	      mu1_index=i;
	      mu2_index=j;
	      check = 1;

	      eta1 = muon_eta[i];
	    } 
	}
      }
    }
    
    //Look for a second muon pair, making sure not to reuse the same muons that you just used.
    if (check==1) {
      for (int i=0 ; i<4 ; i++) {
	if ((i!=mu1_index) and (i!=mu2_index)) {
	  for (int j=0 ; j<4 ; j++) {
	    if ((j!= i) and (j!=mu1_index) and (j!=mu2_index)) {

	      //Check that this new muon pair is in a different endcap than the other pair.
	      if (((eta1 * muon_eta[i]) < 0) and ((muon_eta[i] * muon_eta[j]) > 0) and (reco::deltaR(muon_eta[i], muon_phi[i], muon_eta[j], muon_phi[j]) < 0.5)) {
		return true;
	      } 
	    }
          }
	}
      }
    }
  }

  return false;
}


// ------------ method called once each job just before starting event loop  ------------
void
FilterSample2GenMu::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
FilterSample2GenMu::endJob()
{
}

// ------------ method called when starting to processes a run  ------------
void
FilterSample2GenMu::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
FilterSample2GenMu::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
FilterSample2GenMu::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
FilterSample2GenMu::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
FilterSample2GenMu::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//Indentation change
//define this as a plug-in
DEFINE_FWK_MODULE(FilterSample2GenMu);
