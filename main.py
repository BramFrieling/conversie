def on_button_pressed_a():
    global binair
    binair = "" + binair + "1"
input.on_button_pressed(Button.A, on_button_pressed_a)

def converteer(binairGetal: str):
    global totaal
    totaal = 0
    index = 0
    while index <= len(binairGetal) - 1:
        totaal = totaal + 2 ** index * parse_float(binairGetal.char_at(index))
        index += 1

def on_button_pressed_ab():
    global omgekeerdeTekst
    omgekeerdeTekst = keerOm(binair)
    converteer(omgekeerdeTekst)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def keerOm(input2: str):
    global omkeren
    omkeren = ""
    for waarde in input2:
        omkeren = "" + waarde + omkeren
    return omkeren

def on_button_pressed_b():
    global binair
    binair = "" + binair + "0"
input.on_button_pressed(Button.B, on_button_pressed_b)

def som(getal1: number, getal2: number):
    global uitkomst
    uitkomst = getal1 + getal2
    return uitkomst
uitkomst = 0
omkeren = ""
omgekeerdeTekst = ""
totaal = 0
binair = ""
binair = ""