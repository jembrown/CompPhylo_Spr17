#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 14:59:50 2017

@author: cw
"""
import random
class sampling:
 def __init__(self,eventList=[],probList=[]):
     self.eventList=eventList
     self.probList=probList
     
 def sample(self):
    addedProb=[]
    prob=self.probList
    events=self.eventList
    for id_,i in enumerate(prob):
    
        if id_==0:
            addedProb.append(i)
        else:
            nex=i+addedProb[id_-1]
            #print(nex)
            addedProb.append(nex)
    a=[0 ] 
    zaddedProb=a+addedProb   
   # print(zaddedProb)
    x=random.uniform(0, 1)
    for zidx,zi in enumerate(zaddedProb):
        if zi<x<zaddedProb[zidx+1]:
        
            return (events[zidx])
        else:
         continue

class mChain:
    #sampledStates=[]
    #sam=sample()
    # constructor for the class, take arguments state 
    sampledStates=[]
    def __init__(self,stateSpace,tM,curr_state):
        # initilize all the variables
        self.stateSpace=stateSpace
        self.tM=tM
        self.sampledStates.append(curr_state)
    # function to check all the vaiables are correctly initilized   
    def prin1(self):
        return (self.stateSpace)
    def prin3(self):
        return self.tm
   # def prin4(self):
      #  return self.initial_prob
    #def runM():
    #ss=mChain.stateSpace
    def nextState(self):
         """ get the tansition probabilities for next step"""
         # get the current state
         current_state=self.sampledStates[-1]
         #use current state to get probabilites for next state from TM
         state_prob=self.tM[self.stateSpace.index(current_state)]
         # pass the list of probs and state spaces to get the next value
         sampler=sampling(self.stateSpace,state_prob)
         # append the new state into sampled state list
         self.sampledStates.append(sampler.sample())
         
    def clear(self):
        """" This function clears the sam"""
        self.sampledStates=[self.sampledStates[0]]

    def return_ss(self):
        return self.sampledStates
        
       
        
        
    
        
s=["s","d"] 
t=[[0.4,0.6],[0.5,0.5]] 
in_="s"    

#eeList=["a","b"]
#ppList=[0.5,0.5]

list_for_each_chain=[]
mc=mChain(s,t,in_)
print(mc.sampledStates)
for i in range(100):
  for j in range(100):
   mc.nextState()
  mc_states=mc.sampledStates
  
  list_for_each_chain.append(mc_states)
  mc.clear()
#print(list_for_each_chain[0])

specifeid_st_list=[]
for one_chain in list_for_each_chain:
    specifeid_st_list.append(one_chain[-1])
print(specifeid_st_list)   
print(specifeid_st_list.count("s"))
#print(len(list_for_each_chain[0]))
#for i in range(len(list_for_each_chain)):
    
    
    

#samp=sampling(eeList,ppList)
#print(samp.sample())
#print(mc.generations)
#print(yy)
