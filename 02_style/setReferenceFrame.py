<<<<<<< HEAD
# created by Luciano Cequinel
# version 2.0.0
# realease date 12/16/2021


import nuke

def changeFrame():

    supportedNodes = ['Tracker4', 'FrameHold', 'Roto', 'Transform', 'CornerPin2D']
   
    selNode = nuke.selectedNodes()

    if len (selNode) == 0:
        nuke.message('Select something!')

    else:
        for node in selNode:
            if node.Class() in supportedNodes:

                if node.knob('reference_frame'):
                    node['reference_frame'].setValue(nuke.frame())
                    print ('%s.reference_frame new value: %s' % (node.name(), (nuke.frame())))

                elif node.knob('first_frame'):
                    node['first_frame'].setValue(nuke.frame())
                    print ('%s.first_frame new value: %s' % (node.name(), (nuke.frame())))

                elif node.knob('ref_frame'):
                    node['ref_frame'].setValue(nuke.frame())
                    print ('%s.ref_frame new value: %s' % (node.name(), (nuke.frame())))


            else:
                print ("%s doesn't have a valid knob:" % (node.name()))



#Add a menu and assign a shortcut
toolbar = nuke.menu('Nodes')
cqnTools = toolbar.addMenu('CQNTools', 'Modify.png')
cqnTools.addCommand('Change reference frame', 'setRefFrame.changeFrame()', 'crtl + shift + alt + f', icon = 'TimeOffset.png')
=======
#******************************************************
# content: simple script to quickly update reference frame on a selected list of nodes
# if the option to use current frame, or to write a specific one
#
# version: 2.2.0
# date: July 31 2022
#
# how to: getFrameUI()
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


def changeFrame(newFrame, node):
   
    for knob in node.knobs():
        if knob in SUPPORTED_KNOBS:
            node[knob].setValue(int(newFrame))
            print ('{}.{} got the value: {}'.format (node.name(), (knob), newFrame))


def getCurrentFrame():
    '''
    use the current frame from current viewer
    '''
    newFrame = nuke.frame()
    selNodes = nuke.selectedNodes()

    if len (selNodes) > 0:
        for node in selNodes:
            if node.Class() in SUPPORTED_NODES:
                changeFrame(newFrame, node)

    else:
        nuke.message('Select some valid node\n{}!'.format (SUPPORTED_NODES))
        return


def getFrameUI():
    '''
    get a specific frame from user
    '''

    selNodes = nuke.selectedNodes()

    validNodes = []

    for node in selNodes:
        if node.Class() in SUPPORTED_NODES:
            validNodes.append(node)

    if len (validNodes) > 0:

        newFrame = (nuke.getInput('frame' '%s' % nuke.frame()))

        if newFrame.isdigit():
            for node in validNodes:
                changeFrame(newFrame, node)
        else:
            nuke.message('You must write an integer value! (e.g 1055)')
            getFrameUI()

    else:
        nuke.message('Select some valid node\n{}!'.format (SUPPORTED_NODES))
        return

#################################
#Add to Nodes menu
toolbar = nuke.menu('Nodes')
cqnTools = toolbar.addMenu('CQNTools', 'Modify.png')
cqnTools.addCommand('Set to this frame', 'setReferenceFrame.getCurrentFrame()')
cqnTools.addCommand('Set to specific frame', 'setReferenceFrame.getFrameUI()')


##########################
# main function
if __name__ == '__main__':
    getFrameUI()

>>>>>>> develop
