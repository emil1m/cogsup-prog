from expyriment import design, control, stimuli, misc

exp = design.Experiment(name="find the circle")
control.initialize(exp)
 # Like circle.py; enables data if needed
fixation = stimuli.FixCross()


red = (255, 0, 0)


circle = stimuli.Circle(radius=50, colour=red, position=(-300, 0))
rectangle = stimuli.Rectangle(size=(100, 100), colour=red, position=(300, 0))

cue = stimuli.TextLine("left or right")
cue.present(clear=True, update=True)
exp.clock.wait(1000)

circle.present(clear=True, update=True)
rectangle.present(clear=False, update=True)
exp.clock.wait(2000)

key, rt = exp.keyboard.wait(keys=[misc.constants.K_LEFT, misc.constants.K_RIGHT])

feedback_text = "CORRECT" if key == misc.constants.K_LEFT else "WRONG"
feedback = stimuli.TextLine(feedback_text)
feedback.present(clear=True, update=True)
exp.clock.wait(3000)

control.end()
