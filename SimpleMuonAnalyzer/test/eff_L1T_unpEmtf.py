# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
print '------> Setting Environment'

import sys
import math
from ROOT import *
import numpy as np
from array import *
import Helper as h

print '------> Importing Root File'

## Configuration settings
MAX_EVT  = -1 ## Maximum number of events to process
PRT_EVT  = 10000 ## Print every Nth event

## L1NTuple branches
evt_tree  = TChain('SimpleMuonAnalyzer/Events')

#dir1 = 'root://cmsxrootd.fnal.gov//store/user/mdecaro/SingleMuon/SingleMuon_Run2018D-ZMu-PromptReco-v2_RAW-RECO-Unpacked/191211_212229/0000/Ntuples/'
#dir1 = 'root://cmsxrootd.fnal.gov//store/user/mdecaro/SingleMuon/SingleMuon_Run2017C-17Nov2017-v1_useParent/200103_210545/0000/Ntuples/'
dir1 = 'root://cmsxrootd.fnal.gov//store/user/mdecaro/SingleMuon/SingleMuon_Run2017C-17Nov2017-v1_useParent/200103_210545/0000/Ntuples2/'
#dir2 = 'root://cmsxrootd.fnal.gov//store/user/mdecaro/SingleMuon/SingleMuon_Run2017B-17Nov2017-v1_useParent/200103_205953/0000/Ntuples/'
#dir1 = 'root://cmsxrootd.fnal.gov//store/user/mdecaro/SingleMuon/SingleMuon_Run2017B-17Nov2017-v1_Parent_noPTCut/200106_163314/0000/Ntuples/'

run_str = '_2018D'


## Load input files
#i = 15
#while  i<485:  #1255
    #file_name = dir1+"L1Ntuple_"+str(i)+".root"
    #print 'Loading file:', "L1Ntuple_"+str(i)+".root"
    #evt_tree.Add(file_name)
    #i+=1

#i = 1
#while  i<2:  #17Nov2017B  240 files
    #file_name = dir1+"L1Ntuple_"+str(i)+".root"
    #print 'Loading file:', "L1Ntuple_"+str(i)+".root"
    #evt_tree.Add(file_name)
    #i+=1

#i = 1
#while  i<262:  #17Nov2017C N1  519 files
    #file_name = dir1+"L1Ntuple_"+str(i)+".root"
    #print 'Loading file:', "L1Ntuple_"+str(i)+".root"
    #evt_tree.Add(file_name)
    #i+=1

i = 1
while  i<400:  #17Nov2017C N2 (no neighbor removal)  437 files
    file_name = dir1+"L1Ntuple_"+str(i)+".root"
    print 'Loading file:', "L1Ntuple_"+str(i)+".root"
    evt_tree.Add(file_name)
    i+=1

#i = 100   #2017B no pT cut
#while  i<128:  #2017B no pT cut
    #file_name = dir1+"L1Ntuple_"+str(i)+".root"
    #print 'Loading file:', "L1Ntuple_"+str(i)+".root"
    #evt_tree.Add(file_name)
    #i+=1

## ================ Histograms ======================
eta_bins = [256, -2.8, 2.8]
phi_bins = [256, -np.pi, np.pi]

h_nEmtf = TH1D('h_nEmtf', '', 8, 0, 8)
h_nReco = TH1D('h_nReco', '', 8, 0, 4)

h_emtf_pt = TH1D('h_emtf_pt', '', 70, 0, 300)
h_emtf1_pt = TH1D('h_emtf1_pt', '', 70, 0, 300)
h_emtf2_pt = TH1D('h_emtf2_pt', '', 70, 0, 300) 
h_emtf_eta = TH1D('h_emtf_eta', '', eta_bins[0], eta_bins[1], eta_bins[2])
h_emtf1_eta = TH1D('h_emtf1_eta', '', eta_bins[0], eta_bins[1], eta_bins[2])
h_emtf2_eta = TH1D('h_emtf2_eta', '', eta_bins[0], eta_bins[1], eta_bins[2])
h_emtf_phi = TH1D('h_emtf_phi', '', phi_bins[0], phi_bins[1], phi_bins[2])
h_emtf1_phi = TH1D('h_emtf1_phi', '', phi_bins[0], phi_bins[1], phi_bins[2])
h_emtf2_phi = TH1D('h_emtf2_phi', '', phi_bins[0], phi_bins[1], phi_bins[2])

h_reco_pt = TH1D('h_reco_pt', '', 256, 0, 1000)
h_reco1_pt = TH1F('','', 256, 0, 1000)
h_reco2_pt = TH1F('h_reco2_pt', '', 256, 0, 250)
h_reco_eta = TH1D('h_reco_eta', '', eta_bins[0], eta_bins[1], eta_bins[2])
h_reco1_eta = TH1D('h_reco1_eta', '', eta_bins[0], eta_bins[1], eta_bins[2])
h_reco2_eta = TH1D('h_reco2_eta', '', eta_bins[0], eta_bins[1], eta_bins[2])
h_reco_phi = TH1D('h_reco_phi', '', phi_bins[0], phi_bins[1], phi_bins[2])
h_reco1_phi = TH1D('h_reco1_phi', '', phi_bins[0], phi_bins[1], phi_bins[2])
h_reco2_phi = TH1D('h_reco2_phi', '', phi_bins[0], phi_bins[1], phi_bins[2])


h_unpEmtf_pt = TH1D('h_unpEmtf_pt', '', 256, 0, 256)
h_unpEmtf_eta = TH1D('h_unpEmtf_eta', '', 256, -2.8, 2.8)
h_unpEmtf_phi_fp = TH1D('h_unpEmtf_phi', '', 256, -180, 180)

h_dEta_denom = TH1D('h_dEta_denom', '', 64, -0.1, 0.1)
h_dPhi_denom = TH1D('h_dPhi_denom', '', 64, -0.1, 0.1)
h_dR_denom   = TH1D('h_dR_denom', '', 64, 0, 0.1)

h_dEta_numer = TH1D('h_dEta_numer', '', 64, -0.1, 0.1)
h_dPhi_numer = TH1D('h_dPhi_numer', '', 64, -0.1, 0.1)
h_dR_numer   = TH1D('h_dR_numer', '', 64, 0, 0.1)

h_reco1_besttrk_dR = TH1D('h_reco1_besttrk_dR', '', 32, 0, 0.3)
h_reco2_besttrk_dR = TH1D('h_reco2_besttrk_dR', '', 32, 0, 0.3)
h_reco_besttrk_dR = TH1D('h_reco_besttrk_dR', '', 32, 0, 0.3)


none_count       = 0
med_count        = 0
pT_count         = 0
EMTFmatch_count  = 0

## ================================================
# Loop over over events in TFile
for iEvt in range(evt_tree.GetEntries()):
  if MAX_EVT > 0 and iEvt > MAX_EVT: break
  if iEvt % PRT_EVT is 0: print 'Event #', iEvt
  
  evt_tree.GetEntry(iEvt)

  if (evt_tree.reco_eta[0] < -90 or evt_tree.reco_eta[0] < -90): continue
  if (evt_tree.reco_eta[1] < -90 or evt_tree.reco_phi[1] < -90): continue

  unpEmtf_Pt, unpEmtf_Eta, unpEmtf_Phi_fp, unpEmtf_Mode_neighbor = [], [], [], []
  unpEmtf_Phi_glob, unpEmtf_Phi = [], []
  unpEmtf_Pt_Good, unpEmtf_Eta_Good, unpEmtf_Phi_Good, unpEmtf_Phi_glob_Good  = [], [], [], [] 

  #Default values in ntuples are -99, so get rid of any event not defined correctly.
  for i in range(len(evt_tree.unpEmtf_Pt)):
    if ((evt_tree.unpEmtf_Pt[i] > -90) and (evt_tree.unpEmtf_Eta[i] > -90) and (evt_tree.unpEmtf_Phi_fp[i] > -90)):
      unpEmtf_Pt.append(evt_tree.unpEmtf_Pt[i])
      unpEmtf_Eta.append(evt_tree.unpEmtf_Eta[i])
      unpEmtf_Phi_fp.append(evt_tree.unpEmtf_Phi_fp[i])
      unpEmtf_Phi.append(evt_tree.unpEmtf_Phi[i])
      unpEmtf_Phi_glob.append(evt_tree.unpEmtf_Phi_glob[i])


  if len(unpEmtf_Pt)!=0:
    unpEmtf_Pt_Good.append(unpEmtf_Pt[0])
    unpEmtf_Eta_Good.append(unpEmtf_Eta[0])
    unpEmtf_Phi_Good.append(unpEmtf_Phi[0])
    unpEmtf_Phi_glob_Good.append(unpEmtf_Phi_glob[0]*np.pi/180.)

  i=1
  while i<len(unpEmtf_Phi):
    j=0
    check=0
    while j<len(unpEmtf_Phi_Good):
      if abs(unpEmtf_Phi_fp[i] - unpEmtf_Phi_fp[j]) == 3600: check+=1
      if abs(unpEmtf_Phi_glob[i] - unpEmtf_Phi_glob[j]) == 0: check+=1
      j+=1
    
    if check==0: 
      unpEmtf_Pt_Good.append(unpEmtf_Pt[i])
      unpEmtf_Eta_Good.append(unpEmtf_Eta[i])
      unpEmtf_Phi_Good.append(unpEmtf_Phi[i])
      unpEmtf_Phi_glob_Good.append(unpEmtf_Phi_glob[i]*np.pi/180.)
    i+=1
  

  h_nReco.Fill(len(evt_tree.reco_eta))
  h_nEmtf.Fill(len(unpEmtf_Pt_Good))

  #Order the offline reco muons, leading and subleading.
  reco_pT = [] #First muon = leading, second muon = subleading
  reco_eta = []
  reco_eta_prop = []
  reco_phi = []
  reco_phi_prop = []

  if evt_tree.reco_pt[0] > evt_tree.reco_pt[1]: 
    reco_pT.append(evt_tree.reco_pt[0])
    reco_pT.append(evt_tree.reco_pt[1])
    reco_eta.append(evt_tree.reco_eta[0])
    reco_eta.append(evt_tree.reco_eta[1])
    reco_eta_prop.append(evt_tree.reco_eta_prop[0])
    reco_eta_prop.append(evt_tree.reco_eta_prop[1])
    reco_phi_prop.append(evt_tree.reco_phi_prop[0])
    reco_phi_prop.append(evt_tree.reco_phi_prop[1])
    reco_phi.append(evt_tree.reco_phi[0])
    reco_phi.append(evt_tree.reco_phi[1])
  if evt_tree.reco_pt[0] < evt_tree.reco_pt[1]:
    reco_pT.append(evt_tree.reco_pt[1])
    reco_pT.append(evt_tree.reco_pt[0])
    reco_eta.append(evt_tree.reco_eta[1])
    reco_eta.append(evt_tree.reco_eta[0])
    reco_eta_prop.append(evt_tree.reco_eta_prop[1])
    reco_eta_prop.append(evt_tree.reco_eta_prop[0])
    reco_phi_prop.append(evt_tree.reco_phi_prop[1])
    reco_phi_prop.append(evt_tree.reco_phi_prop[0])
    reco_phi.append(evt_tree.reco_phi[1])
    reco_phi.append(evt_tree.reco_phi[0])

  if evt_tree.reco_pt[0] == evt_tree.reco_pt[1]: continue
  if len(reco_pT)!=2: continue

  h_reco1_pt.Fill(reco_pT[0])
  h_reco1_eta.Fill(reco_eta[0])
  h_reco1_phi.Fill(reco_phi[0])

  h_reco2_pt.Fill(reco_pT[1])
  h_reco2_eta.Fill(reco_eta[1])
  h_reco2_phi.Fill(reco_phi[1])

  j=0
  while j<len(evt_tree.reco_pt):
    h_reco_pt.Fill(reco_pT[j])
    h_reco_eta.Fill(reco_eta[j])
    h_reco_phi.Fill(reco_phi[j])
    j+=1


  j=0
  while j<len(unpEmtf_Pt_Good):
    if j==0: 
      h_emtf_pt.Fill(unpEmtf_Pt_Good[j])
      h_emtf_eta.Fill(unpEmtf_Eta_Good[j])
      h_emtf_phi.Fill(unpEmtf_Phi_glob_Good[j])

      h_emtf1_pt.Fill(unpEmtf_Pt_Good[j])
      h_emtf1_eta.Fill(unpEmtf_Eta_Good[j])
      h_emtf1_phi.Fill(unpEmtf_Phi_glob_Good[j])

    if j==1:
      h_emtf_pt.Fill(unpEmtf_Pt_Good[j])
      h_emtf_eta.Fill(unpEmtf_Eta_Good[j])
      h_emtf_phi.Fill(unpEmtf_Phi_glob_Good[j])

      h_emtf2_pt.Fill(unpEmtf_Pt_Good[j])
      h_emtf2_eta.Fill(unpEmtf_Eta_Good[j])
      h_emtf2_phi.Fill(unpEmtf_Phi_glob_Good[j])
    j+=1



  best1=0
  best2=0
  best1_backup=0
  best2_backup=0

  j=0
  b1_index=-1
  while j<len(unpEmtf_Phi_glob_Good):
    if (reco_phi_prop[0] - unpEmtf_Phi_glob_Good[j]) > 3.14:  dPhiNorm = (reco_phi_prop[0] - unpEmtf_Phi_glob_Good[j]) - (2*3.14)
    if (reco_phi_prop[0] - unpEmtf_Phi_glob_Good[j]) < -3.14: dPhiNorm = (reco_phi_prop[0] - unpEmtf_Phi_glob_Good[j]) + (2*3.14)
    if (reco_phi_prop[0] - unpEmtf_Phi_glob_Good[j]) <= 3.14 and (reco_phi_prop[0] - unpEmtf_Phi_glob_Good[j]) >= -3.14: dPhiNorm = (reco_phi_prop[0] - unpEmtf_Phi_glob_Good[j])

    if j==0: best1 = h.CalcDR(reco_eta_prop[0], unpEmtf_Eta_Good[j], dPhiNorm)
    if j==1: 
      if h.CalcDR(reco_eta_prop[0], unpEmtf_Eta_Good[j], dPhiNorm) < best1:
	best1_backup = best1
	best1 = h.CalcDR(reco_eta_prop[0], unpEmtf_Eta_Good[j], dPhiNorm)
	b1_index=1
      if h.CalcDR(reco_eta_prop[0], unpEmtf_Eta_Good[j], dPhiNorm) > best1:
	b1_index=0
	best1_backup = h.CalcDR(reco_eta_prop[0], unpEmtf_Eta_Good[j], dPhiNorm)
    j+=1


  #Use the propagated phi to match to Emtf tracks. (First, renorm from -pi to pi, then calc dR)

  j=0
  b2_index=-1
  while j<len(unpEmtf_Phi_glob_Good):
    if (reco_phi_prop[1] - unpEmtf_Phi_glob_Good[j]) > 3.14:  dPhiNorm = (reco_phi_prop[1] - unpEmtf_Phi_glob_Good[j]) - (2*3.14)
    if (reco_phi_prop[1] - unpEmtf_Phi_glob_Good[j]) < -3.14: dPhiNorm = (reco_phi_prop[1] - unpEmtf_Phi_glob_Good[j]) + (2*3.14)
    if (reco_phi_prop[1] - unpEmtf_Phi_glob_Good[j]) <= 3.14 and (reco_phi_prop[1] - unpEmtf_Phi_glob_Good[j]) >= -3.14: dPhiNorm = (reco_phi_prop[1] - unpEmtf_Phi_glob_Good[j])

    if j==0: best2 = h.CalcDR(reco_eta_prop[1], unpEmtf_Eta_Good[j], dPhiNorm)
    if j==1: 
      if h.CalcDR(reco_eta_prop[1], unpEmtf_Eta_Good[j], dPhiNorm) < best2:
	best2_backup = best2
	best2 = h.CalcDR(reco_eta_prop[1], unpEmtf_Eta_Good[j], dPhiNorm)
	b2_index=1
      if h.CalcDR(reco_eta_prop[1], unpEmtf_Eta_Good[j], dPhiNorm) > best2:
	b2_index=0
	best2_backup = h.CalcDR(reco_eta_prop[1], unpEmtf_Eta_Good[j], dPhiNorm)

    j+=1

  if len(unpEmtf_Pt_Good)==2:
    if b1_index==b2_index:
      if best1>best2: best1=best1_backup
      if best2>best1: best2=best2_backup

    h_reco1_besttrk_dR.Fill(best1)
    h_reco2_besttrk_dR.Fill(best2)
    h_reco_besttrk_dR.Fill(best1)
    h_reco_besttrk_dR.Fill(best2)
  
  #print '-------------------------------'
  #print 'reco muon1 pt, prop eta, prop phi:', reco_pT[0], reco_eta_prop[0], reco_phi_prop[0]
  #print 'reco muon2 pt, prop eta, prop phi:', reco_pT[1], reco_eta_prop[1], reco_phi_prop[1]
  #print len(unpEmtf_Eta_Good), ' tracks in the event.'
  #i=0
  #while i<len(unpEmtf_Eta_Good):
    #print 'emtf trk', i, 'pt, eta, phi:', unpEmtf_Pt_Good[i], unpEmtf_Eta_Good[i], unpEmtf_Phi_glob_Good[i]
    #i+=1

  #if len(unpEmtf_Eta_Good)==2:
  ##printouts
    #print len(unpEmtf_Eta_Good)
    #print 'reco muon1 pt, prop eta, prop phi:', reco_pT[0], reco_eta_prop[0], reco_phi_prop[0]
    #print 'reco muon2 pt, prop eta, prop phi:', reco_pT[1], reco_eta_prop[1], reco_phi_prop[1]
    #print 'emtf trk1 pt, eta, phi:', unpEmtf_Pt_Good[0], unpEmtf_Eta_Good[0], unpEmtf_Phi_glob_Good[0]
    #print 'emtf trk2 pt, eta, phi:', unpEmtf_Pt_Good[1], unpEmtf_Eta_Good[1], unpEmtf_Phi_glob_Good[1]
    #print best1, best2
    #print '------------------------------'

  none_count+=1

  if evt_tree.reco_isMediumMuon[0] != 1 or evt_tree.reco_isMediumMuon[1] != 1: continue
  med_count+=1

  h_dEta_denom.Fill(reco_eta[0] - reco_eta[1])
  h_dPhi_denom.Fill(reco_phi[0] - reco_phi[1])
  h_dR_denom.Fill(h.CalcDR2(reco_eta[0], reco_phi[0], reco_eta[1], reco_phi[1]))

  if best1>0.3 or best2>0.3 or len(unpEmtf_Eta_Good)<2: continue
  EMTFmatch_count+=1

  h_dEta_numer.Fill(reco_eta[0] - reco_eta[1])
  h_dPhi_numer.Fill(reco_phi[0] - reco_phi[1])
  h_dR_numer.Fill(h.CalcDR2(reco_eta[0], reco_phi[0], reco_eta[1], reco_phi[1]))

#Printouts
print '-------------'
print 'nMuons after selections:'
print 'pre-selections only:', none_count
print 'both reco muons are medium ID:', med_count
#print 'both reco muons pT > 26 GeV:', pT_count
print 'both muons are EMTF matched:', EMTFmatch_count
############################################################
### Write output file with histograms and efficiencies ###
############################################################

##c1 = TCanvas( 'c1', 'test scatter', 200, 10, 700, 500)
##gPad.SetLogy()
##h_reco_pt.SetMinimum(1)
##h_reco_pt.Draw()
##gStyle.SetOptStat(0)
##h_reco_pt.SetTitle('All offline reco muon pT')
##h_reco_pt.GetXaxis().SetTitle('pT (GeV)')
##h_reco_pt.Write()
##c1.SaveAs("trees/reco_pT.png")
##c1.Close()

#c2 = TCanvas( 'c2', '', 200, 10, 700, 500)
#gPad.SetLogy()
#h_reco1_pt.SetMinimum(1)
#h_reco1_pt.Draw()
#gStyle.SetOptStat(0)
#h_reco1_pt.GetXaxis().SetTitle('pT (GeV)')
#h_reco1_pt.SetTitle('First offline reco muon pT')
#h_reco1_pt.Write()
#c2.SaveAs("trees/reco1_pT.png")
#c2.Close()

#c3 = TCanvas( 'c1', 'test scatter', 200, 10, 700, 500)
#gPad.SetLogy()
#h_reco2_pt.SetMinimum(1)
#h_reco2_pt.Draw()
#gStyle.SetOptStat(0)
#h_reco2_pt.SetTitle('Second offline reco muon pT')
#h_reco2_pt.GetXaxis().SetTitle('pT (GeV)')
#h_reco2_pt.Write()
#c3.SaveAs("trees/reco2_pT.png")
#c3.Close()

##c4 = TCanvas( 'c1', 'test scatter', 200, 10, 700, 500)
##gPad.SetLogy()
##h_reco_eta.SetMinimum(1)
##h_reco_eta.Draw()
##gStyle.SetOptStat(0)
##h_reco_eta.SetTitle('All offline reco muon #eta')
##h_reco_eta.GetXaxis().SetTitle('#eta')
##h_reco_eta.Write()
##c4.SaveAs("trees/reco_eta.png")
##c4.Close()

#c5 = TCanvas( 'c1', 'test scatter', 200, 10, 700, 500)
#gPad.SetLogy()
#h_reco1_eta.SetMinimum(1)
#h_reco1_eta.Draw()
#gStyle.SetOptStat(0)
#h_reco1_eta.SetTitle('First offline reco muon #eta')
#h_reco1_eta.GetXaxis().SetTitle('#eta')
#h_reco1_eta.Write()
#c5.SaveAs("trees/reco1_eta.png")
#c5.Close()

#c5 = TCanvas( 'c1', 'test scatter', 200, 10, 700, 500)
#gPad.SetLogy()
#h_reco2_eta.SetMinimum(1)
#h_reco2_eta.Draw()
#gStyle.SetOptStat(0)
#h_reco2_eta.SetTitle('Second offline reco muon #eta')
#h_reco2_eta.GetXaxis().SetTitle('#eta')
#h_reco2_eta.Write()
#c5.SaveAs("trees/reco2_eta.png")
#c5.Close()

###c6 = TCanvas( 'c1', 'test scatter', 200, 10, 700, 500)
###gPad.SetLogy()
###h_reco_phi.SetMinimum(1)
###h_reco_phi.Draw()
###gStyle.SetOptStat(0)
###h_reco_phi.SetTitle('All offline reco muon #phi')
###h_reco_phi.GetXaxis().SetTitle('#phi')
###h_reco_phi.Write()
###c6.SaveAs("trees/reco_phi.png")
###c6.Close()

#c7 = TCanvas( 'c1', 'test scatter', 200, 10, 700, 500)
#gPad.SetLogy()
#h_reco1_phi.SetMinimum(1)
#h_reco1_phi.Draw()
#gStyle.SetOptStat(0)
#h_reco1_phi.SetTitle('First offline reco muon #phi')
#h_reco1_phi.GetXaxis().SetTitle('#phi')
#h_reco1_phi.Write()
#c7.SaveAs("trees/reco1_phi.png")
#c7.Close()

#c8 = TCanvas( 'c1', 'test scatter', 200, 10, 700, 500)
#gPad.SetLogy()
#h_reco2_phi.SetMinimum(1)
#h_reco2_phi.Draw()
#gStyle.SetOptStat(0)
#h_reco2_phi.SetTitle('Second offline reco muon #phi')
#h_reco2_phi.GetXaxis().SetTitle('#phi')
#h_reco2_phi.Write()
#c8.SaveAs("trees/reco2_phi.png")
#c8.Close()

##c12 = TCanvas( 'c1', 'test scatter', 200, 10, 700, 500)
##gPad.SetLogy()
##h_emtf_pt.SetMinimum(1)
##h_emtf_pt.Draw()
##gStyle.SetOptStat(0)
##h_emtf_pt.SetTitle('All EMTF Tracks pT')
##h_emtf_pt.GetXaxis().SetTitle('pT (GeV)')
##h_emtf_pt.Write()
##c12.SaveAs("trees/emtf_pT.png")
##c12.Close()

#c13 = TCanvas( 'c1', 'test scatter', 200, 10, 700, 500)
#gPad.SetLogy()
#h_emtf1_pt.SetMinimum(1)
#h_emtf1_pt.Draw()
#gStyle.SetOptStat(0)
#h_emtf1_pt.SetTitle('First Emtf track pT')
#h_emtf1_pt.GetXaxis().SetTitle('pT (GeV)')
#h_emtf1_pt.Write()
#c13.SaveAs("trees/emtf1_pT.png")
#c13.Close()

#c14 = TCanvas( 'c1', 'test scatter', 200, 10, 700, 500)
#gPad.SetLogy()
#h_emtf2_pt.SetMinimum(1)
#h_emtf2_pt.Draw()
#gStyle.SetOptStat(0)
#h_emtf2_pt.SetTitle('Second Emtf track pT')
#h_emtf2_pt.GetXaxis().SetTitle('pT (GeV)')
#h_emtf2_pt.Write()
#c14.SaveAs("trees/emtf2_pT.png")
#c14.Close()

##c16 = TCanvas( 'c1', 'test scatter', 200, 10, 700, 500)
##gPad.SetLogy()
##h_emtf_eta.SetMinimum(1)
##h_emtf_eta.Draw()
##gStyle.SetOptStat(0)
##h_emtf_eta.SetTitle('All EMTF tracks #eta')
##h_emtf_eta.GetXaxis().SetTitle('#eta')
##h_emtf_eta.Write()
##c16.SaveAs("trees/emtf_eta.png")
##c16.Close()

#c17 = TCanvas( 'c1', 'test scatter', 200, 10, 700, 500)
#gPad.SetLogy()
#h_emtf1_eta.SetMinimum(1)
#h_emtf1_eta.Draw()
#gStyle.SetOptStat(0)
#h_emtf1_eta.SetTitle('First Emtf track #eta')
#h_emtf1_eta.GetXaxis().SetTitle('#eta')
#h_emtf1_eta.Write()
#c17.SaveAs("trees/emtf1_eta.png")
#c17.Close()

#c18 = TCanvas( 'c1', 'test scatter', 200, 10, 700, 500)
#gPad.SetLogy()
#h_emtf2_eta.SetMinimum(1)
#h_emtf2_eta.Draw()
#gStyle.SetOptStat(0)
#h_emtf2_eta.SetTitle('Second Emtf track #eta')
#h_emtf2_eta.GetXaxis().SetTitle('#eta')
#h_emtf2_eta.Write()
#c18.SaveAs("trees/emtf2_eta.png")
#c18.Close()

##c20 = TCanvas( 'c1', 'test scatter', 200, 10, 700, 500)
##gPad.SetLogy()
##h_emtf_phi.SetMinimum(1)
##h_emtf_phi.Draw()
##gStyle.SetOptStat(0)
##h_emtf_phi.SetTitle('All EMTF tracks #phi')
##h_emtf_phi.GetXaxis().SetTitle('#phi')
##h_emtf_phi.Write()
##c20.SaveAs("trees/emtf_phi.png")
##c20.Close()

#c21 = TCanvas( 'c1', 'test scatter', 200, 10, 700, 500)
#gPad.SetLogy()
#h_emtf1_phi.SetMinimum(1)
#h_emtf1_phi.Draw()
#gStyle.SetOptStat(0)
#h_emtf1_phi.SetTitle('First emtf track #phi')
#h_emtf1_phi.GetXaxis().SetTitle('#phi')
#h_emtf1_phi.Write()
#c21.SaveAs("trees/emtf1_phi.png")
#c21.Close()

#c22 = TCanvas( 'c1', 'test scatter', 200, 10, 700, 500)
#gPad.SetLogy()
#h_emtf2_phi.SetMinimum(1)
#h_emtf2_phi.Draw()
#gStyle.SetOptStat(0)
#h_emtf2_phi.SetTitle('Second emtf track #phi')
#h_emtf2_phi.GetXaxis().SetTitle('#phi')
#h_emtf2_phi.Write()
#c22.SaveAs("trees/emtf2_phi.png")
#c22.Close()

#c33 = TCanvas( 'c1', 'test scatter', 200, 10, 700, 500)
#gPad.SetLogy()
#h_nReco.SetMinimum(1)
#h_nReco.Draw()
#gStyle.SetOptStat(0)
#h_nReco.SetTitle('Number of Offline Reconstructed Muons per event')
#h_nReco.GetXaxis().SetTitle('Offline Muons')
#h_nReco.Write()
#c33.SaveAs("trees/nReco.png")
#c33.Close()

#c34 = TCanvas( 'c1', 'test scatter', 200, 10, 700, 500)
#gPad.SetLogy()
#h_nEmtf.SetMinimum(1)
#h_nEmtf.Draw()
#gStyle.SetOptStat(0)
#h_nEmtf.SetTitle('Number of EMTF tracks per event')
#h_nEmtf.GetXaxis().SetTitle('EMTF Tracks')
#h_nEmtf.Write()
#c34.SaveAs("trees/nEmtf.png")
#c34.Close()

#c51 = TCanvas( 'c1', 'test scatter', 200, 10, 700, 500)
#gPad.SetLogy()
#h_reco1_besttrk_dR.SetMinimum(1)
#h_reco1_besttrk_dR.Draw()
#gStyle.SetOptStat(0)
#h_reco1_besttrk_dR.SetTitle('#Delta R of first offline muon with closest Emtf track')
#h_reco1_besttrk_dR.GetXaxis().SetTitle('#Delta R')
#h_reco1_besttrk_dR.Write()
#c51.SaveAs("tests2/reco1_emtf_best_dR.png")
#c51.Close()

#c52 = TCanvas( 'c1', 'test scatter', 200, 10, 700, 500)
#gPad.SetLogy()
#h_reco2_besttrk_dR.SetMinimum(1)
#h_reco2_besttrk_dR.Draw()
#gStyle.SetOptStat(0)
#h_reco2_besttrk_dR.SetTitle('#Delta R of second offline muon with closest Emtf track')
#h_reco2_besttrk_dR.GetXaxis().SetTitle('#Delta R')
#h_reco2_besttrk_dR.Write()
#c52.SaveAs("tests2/reco2_emtf_best_dR.png")
#c52.Close()
##c53 = TCanvas( 'c1', 'test scatter', 200, 10, 700, 500)
##gPad.SetLogy()
##h_reco_besttrk_dR.SetMinimum(1)
##h_reco_besttrk_dR.Draw()
##h_reco_besttrk_dR.SetTitle('#Delta R of both reco muons with their respective closest Emtf tracks')
##h_reco_besttrk_dR.GetXaxis().SetTitle('#Delta R')
##h_reco_besttrk_dR.Write()
##c53.SaveAs("tests2/reco_emtf_best_dR.png")
##c53.Close()



c57 = TCanvas( 'c1', 'eff', 200, 10, 700, 500)
c57.SetGrid()
eff = TEfficiency(h_dEta_numer, h_dEta_denom)
eff.Draw()
eff.SetTitle('Trigger Efficiency vs #Delta #eta')
gPad.Update()
graph = eff.GetPaintedGraph()
graph.SetMinimum(0)
graph.SetMaximum(1)
gPad.Update()
eff.Write()
c57.Update()
c57.Modified()
c57.Update()
c57.SaveAs("tests2/eff_dEta.png")
c57.Close()

c58 = TCanvas( 'c1', 'eff', 200, 10, 700, 500)
c58.SetGrid()
eff2 = TEfficiency(h_dPhi_numer, h_dPhi_denom)
eff2.Draw()
eff2.SetTitle('Trigger Efficiency vs #Delta #phi')
gPad.Update()
graph = eff2.GetPaintedGraph()
graph.SetMinimum(0)
graph.SetMaximum(1)
gPad.Update()
eff2.Write()
c58.Update()
c58.Modified()
c58.Update()
c58.SaveAs("tests2/eff_dPhi.png")
c58.Close()

c59 = TCanvas( 'c1', 'eff', 200, 10, 700, 500)
c59.SetGrid()
eff3 = TEfficiency(h_dR_numer, h_dR_denom)
eff3.Draw()
eff3.SetTitle('Trigger Efficiency vs #Delta R')
gPad.Update()
graph = eff3.GetPaintedGraph()
graph.SetMinimum(0)
graph.SetMaximum(1)
gPad.Update()
eff3.Write()
c59.Update()
c59.Modified()
c59.Update()
c59.SaveAs("tests2/eff_dR.png")
c59.Close()