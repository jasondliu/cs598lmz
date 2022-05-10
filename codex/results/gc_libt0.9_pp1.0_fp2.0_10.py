import gc, weakref, types

from ROOT import TLorentzVector

from PhysicsTools.HeppyCore.utils.cmsswPreprocessor import CmsswPreprocessor
from PhysicsTools.HeppyCore.utils.deltar import deltaR
from PhysicsTools.HeppyCore.papas.pfobjects import  PapasParticle, PapasObjTypes
from PhysicsTools.HeppyCore.papas.pfalgo import PfAlgo
from PhysicsTools.HeppyCore.papas.data.identifier import Identifier
from PhysicsTools.HeppyCore.papas.data.papasevent import PapasEvent
from PhysicsTools.HeppyCore.papas.data.particles import Particle, Electron, Muon, Tau, Photon, Track, Cluster
from PhysicsTools.HeppyCore.papas.data.links import Link, CascadeLink, CollisionLink, SimTrack, InternalLink, SimParticle, SimCluster
from PhysicsTools.HeppyCore.papas.data.graph import FwdGraph, BkwGraph
from PhysicsTools.HeppyCore.papas.
