#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Ivan Vladimir Meza Ruiz 2018
# GPL 3.0

import random

def execute(*args):
    var=args[0]
    opts=args[1]
    msg = random.choice(["En términos generales, la toalla sanitaria debe susti    tuirse cada 4 horas para mantenerte fresca; recuerda que su función     es atrapar la sangre que tu cuerpo está desechando y si permanece la    rgo tiempo en contacto con tu zona íntima, podría favorecer la repro    ducción de bacterias causantes de infección vaginal", "Si tienes algún tipo de síntoma como picazón, enrojec    imiento o molestias, es mejor consultar a tu médico para que te aseg    ures que no se ha generado ninguna infección.", "Envuelve las toallas sanitarias en su mismo envoltori    o y desechalas en el cesto de basura o en alguna bolsa exclusiva par    a este tipo de desecho. Nunca en el WC", ]+opts)
    return 'set_slot {0} "{1}"'.format(var,msg)

