# https://kodim.cz/czechitas/uvod-do-progr-2/bonusy/cykly-2/list-comprehension/promitani

def prevod(vstup):
    return [f"{cas//60}:{cas%60:02d}" for cas in vstup]
