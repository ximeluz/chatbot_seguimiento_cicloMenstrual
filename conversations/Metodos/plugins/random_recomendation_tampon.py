#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Ivan Vladimir Meza Ruiz 2018
# GPL 3.0

import random

def execute(*args):
    var=args[0]
    opts=args[1]
    msg = random.choice(["Si usas tampones recuerda siempre leer las etiquetas y usar el tampón con menos absorción posible.","Alterna usando tampones y toallitas femeninas, usa toallitas más pequeñas cuando el flujo es leve.","Usa la absorbencia que se ajuste a tus necesidades."]+opts)
    return 'set_slot {0} "{1}"'.format(var,msg)

