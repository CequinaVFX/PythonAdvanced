#******************************************************
# content: simple script to quickly update reference frame on a selected node
#
# version: 2.1.0
# date: July 31 2022
#
# how to: 
# dependencies: nuke
# todos: --//--
#
# license: MIT
# author: Luciano Cequinel [lucianocequinel@gmail.com]
#******************************************************

import nuke

##################
# global variables

SUPPORTED_NODES = ['Tracker4', 'FrameHold', 'Roto', 'RotoPaint', 'Transform', 'CornerPin2D', 'VectorDistort']
SUPPORTED_KNOBS = ['reference_frame', 'referenceFrame', 'first_frame', 'ref_frame']

def changeFrame(newFrame, selNodes):
   
    for node in selNodes:

        #if node.Class() in SUPPORTED_NODES:
            
        for knob in node.knobs():
            if knob in SUPPORTED_KNOBS:
                node[knob].setValue(newFrame)
                print ('{}.{} got the value: {}'.format (node.name(), (knob), newFrame))

            else:
                print ("{} doesn't have a valid knob:".format (node.name()))


def getCurrentFrame():
    
    selNodes = nuke.selectedNodes()

    validNodes = []

    for node in selNodes:
        if node.Class() in SUPPORTED_NODES:
            print ('adding node {}'.format (node.name()))
            validNodes.append(node)

    if len (validNodes) == 0:
        nuke.message('Select something!')
        return

    newFrame = nuke.frame()

    changeFrame(newFrame, selNodes)


def getFrameUI():

    selNodes = nuke.selectedNodes()

    if selNodes not in SUPPORTED_NODES:

    validNodes = []

    for node in selNodes:
        if node.Class() in SUPPORTED_NODES:
            print ('adding node {}'.format (node.name()))
            validNodes.append(node)

    if len (validNodes) == 0:
        nuke.message('Select something!')
        return

    newFrame = int(nuke.getInput('frame'))

    changeFrame(newFrame, selNodes)


getCurrentFrame()
#getFrameUI()
#################################
#Add to Nodes menu
#toolbar = nuke.menu('Nodes')
#cqnTools = toolbar.addMenu('CQNTools', 'Modify.png')
#cqnTools.addCommand('Set to this frame', 'setRefFrame.getCurrrentFrame()')
#cqnTools.addCommand('Set to specific frame', 'setRefFrame.getFrameUI()')