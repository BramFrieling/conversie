input.onButtonPressed(Button.A, function () {
    binair = "" + binair + "1"
})
function converteer (binairGetal: string) {
    totaal = 0
    while (index <= binairGetal.length - 1) {
        totaal = totaal + 2 ** index * parseFloat(binairGetal.charAt(index))
        index += 1
    }
    return totaal
}
input.onButtonPressed(Button.AB, function () {
    omgekeerdeTekst = keerOm(binair)
    converteer(omgekeerdeTekst)
})
function keerOm (input2: string) {
    omkeren = ""
    for (let waarde of input2) {
        omkeren = "" + waarde + omkeren
    }
    return omkeren
}
input.onButtonPressed(Button.B, function () {
    binair = "" + binair + "0"
})
function som (getal1: number, getal2: number) {
    uitkomst = getal1 + getal2
    return uitkomst
}
let uitkomst = 0
let omkeren = ""
let omgekeerdeTekst = ""
let index = 0
let totaal = 0
let binair = ""
binair = ""
