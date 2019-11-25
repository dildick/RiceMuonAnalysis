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
  iEvent.getByToken(m_muons, muons);
  const reco::GenParticleCollection& muonC = *muons.product();

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
