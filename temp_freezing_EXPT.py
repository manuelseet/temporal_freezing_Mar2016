#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), May 01, 2016, at 21:32

Manuel Seet - TSP Sem 1 2016

Psychopy experiment for temporal freezing (Motoyoshi, 2008)

"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui, hardware
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
# from the Builder filename that created this script
expName = 'semantic experiment'
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + \
    'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath=u'F:\\4 - TSP 2016 (Sem 1) - Temporal Freezing\\My Experiments\\REAL EXPERIMENT\\TRY THIS.psyexp',
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
# this outputs to the screen, not a file
logging.console.setLevel(logging.WARNING)

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1366, 768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
                    monitor='testMonitor', color=[1, 1, 1], colorSpace='rgb',
                    blendMode='avg', useFBO=True,
                    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0  # couldn't get a reliable measure so guess

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
instructions = visual.TextStim(win=win, ori=0, name='instructions',
                               text=u'Welcome to the experiment.\n\nPlease press the spacebar to continue.',    font=u'Arial',
                               pos=[0, 0], height=0.1, wrapWidth=None,
                               color=u'white', colorSpace='rgb', opacity=1,
                               depth=0.0)

# Initialize components for Routine "pic_trial"
pic_trialClock = core.Clock()
mask1 = visual.ImageStim(win=win, name='mask1', units='cm',
                         image='sin', mask=None,
                         ori=0, pos=[0, -9], size=[27, 3],
                         color=[1, 1, 1], colorSpace='rgb', opacity=1,
                         flipHoriz=False, flipVert=False,
                         texRes=128, interpolate=True, depth=0.0)
final = visual.TextStim(win=win, ori=0, name='final',
                        text=u'+',    font=u'Arial',
                        pos=[0, 9], height=0.1, wrapWidth=None,
                        color=u'red', colorSpace='rgb', opacity=1,
                        depth=-1.0)
movie = visual.MovieStim(win=win, name='movie',
                         filename=u'F:\\4 - TSP 2016 (Sem 1) - Temporal Freezing\\My Experiments\\REAL EXPERIMENT\\Concentric_med_medsq_80.swf',
                         ori=0, pos=[0, 0], opacity=1,
                         depth=-3.0,
                         )

# Initialize components for Routine "end"
endClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
                       text='This marks the end of the experiment. \n\nThank you for your participation.',    font='Arial',
                       pos=[0, 0], height=0.1, wrapWidth=None,
                       color='white', colorSpace='rgb', opacity=1,
                       depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
# to track time remaining of each (non-slip) routine
routineTimer = core.CountdownTimer()

# ------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock
frameN = -1
# update component parameters for each repeat
# create an object of type KeyResponse
key_resp_start = event.BuilderKeyResponse()
key_resp_start.status = NOT_STARTED
# keep track of which components have finished
InstructionsComponents = []
InstructionsComponents.append(instructions)
InstructionsComponents.append(key_resp_start)
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *instructions* updates
    if t >= 0.0 and instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions.tStart = t  # underestimates by a little under one frame
        instructions.frameNStart = frameN  # exact frame index
        instructions.setAutoDraw(True)

    # *key_resp_start* updates
    if t >= 1 and key_resp_start.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_start.tStart = t  # underestimates by a little under one frame
        key_resp_start.frameNStart = frameN  # exact frame index
        key_resp_start.status = STARTED
        # keyboard checking is just starting
        key_resp_start.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_start.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_start.keys = theseKeys[-1]  # just the last key pressed
            key_resp_start.rt = key_resp_start.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_start.keys in ['', [], None]:  # No response was made
    key_resp_start.keys = None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_start.keys', key_resp_start.keys)
if key_resp_start.keys != None:  # we had a response
    thisExp.addData('key_resp_start.rt', key_resp_start.rt)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
pictures = data.TrialHandler(nReps=1, method='sequential',
                             extraInfo=expInfo, originPath=u'F:\\4 - TSP 2016 (Sem 1) - Temporal Freezing\\My Experiments\\REAL EXPERIMENT\\TRY THIS.psyexp',
                             trialList=data.importConditions(
                                 u'Picture V2.1.xlsx'),
                             seed=None, name='pictures')
thisExp.addLoop(pictures)  # add the loop to the experiment
# so we can initialise stimuli with some values
thisPicture = pictures.trialList[0]
# abbreviate parameter names if possible (e.g. rgb=thisPicture.rgb)
if thisPicture != None:
    for paramName in thisPicture.keys():
        exec(paramName + '= thisPicture.' + paramName)

for thisPicture in pictures:
    currentLoop = pictures
    # abbreviate parameter names if possible (e.g. rgb = thisPicture.rgb)
    if thisPicture != None:
        for paramName in thisPicture.keys():
            exec(paramName + '= thisPicture.' + paramName)

    # ------Prepare to start Routine "pic_trial"-------
    t = 0
    pic_trialClock.reset()  # clock
    frameN = -1
    # update component parameters for each repeat
    mask1.setImage(M1)
    # create an object of type KeyResponse
    key_resp_14 = event.BuilderKeyResponse()
    key_resp_14.status = NOT_STARTED
    # keep track of which components have finished
    pic_trialComponents = []
    pic_trialComponents.append(mask1)
    pic_trialComponents.append(final)
    pic_trialComponents.append(key_resp_14)
    pic_trialComponents.append(movie)
    for thisComponent in pic_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "pic_trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = pic_trialClock.getTime()
        # number of completed frames (so 0 is the first frame)
        frameN = frameN + 1
        # update/draw components on each frame

        # *mask1* updates
        if t >= 0 and mask1.status == NOT_STARTED:
            # keep track of start time/frame for later
            mask1.tStart = t  # underestimates by a little under one frame
            mask1.frameNStart = frameN  # exact frame index
            mask1.setAutoDraw(True)

        # *final* updates
        if frameN >= 340 and final.status == NOT_STARTED:
            # keep track of start time/frame for later
            final.tStart = t  # underestimates by a little under one frame
            final.frameNStart = frameN  # exact frame index
            final.setAutoDraw(True)

        # *key_resp_14* updates
        if frameN >= 340 and key_resp_14.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_14.tStart = t  # underestimates by a little under one frame
            key_resp_14.frameNStart = frameN  # exact frame index
            key_resp_14.status = STARTED
            # keyboard checking is just starting
            key_resp_14.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_14.status == STARTED:
            theseKeys = event.getKeys(
                keyList=['y', 'n', 'left', 'right', 'space'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_14.keys = theseKeys[-1]  # just the last key pressed
                key_resp_14.rt = key_resp_14.clock.getTime()
                # a response ends the routine
                continueRoutine = False

        # *movie* updates
        if t >= 2 and movie.status == NOT_STARTED:
            # keep track of start time/frame for later
            movie.tStart = t  # underestimates by a little under one frame
            movie.frameNStart = frameN  # exact frame index
            movie.setAutoDraw(True)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pic_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "pic_trial"-------
    for thisComponent in pic_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_14.keys in ['', [], None]:  # No response was made
        key_resp_14.keys = None
    # store data for pictures (TrialHandler)
    pictures.addData('key_resp_14.keys', key_resp_14.keys)
    if key_resp_14.keys != None:  # we had a response
        pictures.addData('key_resp_14.rt', key_resp_14.rt)
    # the Routine "pic_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()

# completed 1 repeats of 'pictures'


# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
# keep track of which components have finished
endComponents = []
endComponents.append(text)
endComponents.append(key_resp_3)
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)

    # *key_resp_3* updates
    if t >= 5 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        key_resp_3.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_3.keys', key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
win.close()
core.quit()
