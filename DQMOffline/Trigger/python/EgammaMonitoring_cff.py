import FWCore.ParameterSet.Config as cms

from DQMOffline.Trigger.HLTEGTnPMonitor_cfi import egmGsfElectronIDsForDQM,egHLTDQMOfflineTnPSource,egmPhotonIDSequenceForDQM,egHLTElePhoDQMOfflineTnPSource,egHLTElePhoHighEtaDQMOfflineTnPSource,photonIDValueMapProducer,egmPhotonIDsForDQM,egHLTMuonPhoDQMOfflineTnPSource,egmDQMSelectedMuons,egmMuonIDSequenceForDQM,egHLTMuonEleDQMOfflineTnPSource

egammaMonitorHLT = cms.Sequence(
    egHLTDQMOfflineTnPSource*
    egmPhotonIDSequenceForDQM*
    egHLTElePhoDQMOfflineTnPSource*
    egHLTElePhoHighEtaDQMOfflineTnPSource*
    egmMuonIDSequenceForDQM*
    egHLTMuonEleDQMOfflineTnPSource*
    egHLTMuonPhoDQMOfflineTnPSource,

    cms.Task(egmGsfElectronIDsForDQM)
)

egmHLTDQMSourceExtra = cms.Sequence(
)
