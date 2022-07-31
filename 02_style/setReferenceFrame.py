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