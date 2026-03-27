from expyriment import design, control, stimuli, misc
import random

exp = design.Experiment(name="find the circle (random position)")
control.initialize(exp)

fixation = stimuli.FixCross()
red = (255, 0, 0)

for trial in range(10):
    circle_left = random.choice([True, False])
    circle_pos = (-300, 0) if circle_left else (300, 0)
    rect_pos = (300, 0) if circle_left else (-300, 0)
    
    circle = stimuli.Circle(radius=50, colour=red, position=circle_pos)
    rectangle = stimuli.Rectangle(size=(100, 100), colour=red, position=rect_pos)
    
    cue = stimuli.TextLine("left or right")
    cue.present(clear=True, update=True)
    exp.clock.wait(1000)
    
    circle.present(clear=True, update=True)
    rectangle.present(clear=False, update=True)
    exp.clock.wait(2000)
    
    key, rt = exp.keyboard.wait(keys=[misc.constants.K_LEFT, misc.constants.K_RIGHT])
    
    feedback_text = "CORRECT" if (key == misc.constants.K_LEFT) == circle_left else "WRONG"
    feedback = stimuli.TextLine(feedback_text)
    feedback.present(clear=True, update=True)
    exp.clock.wait(3000)

control.end()
