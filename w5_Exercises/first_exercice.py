from expyriment import design, control, stimuli


exp = design.Experiment(name="find the circle") 
control.initialize(exp)
rectangle = stimuli.Rectangle(size=(width, height), colour=(R, G, B)) on the right side of the screen
circle = stimuli.Circle(size=(width, height), colour=(R, G, B)) on the left side of the screen

cue = stimuli.TextLine("left or right")
cue.present

key = exp.keyboard.wait()  

if key == expyriment.misc.constants: K_down:
    print("CORRECT")
else:    print("WRONG")


feedback.present()

exp.clock.wait(3000)

control.end()


