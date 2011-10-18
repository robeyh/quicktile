'''
A simple config file with two profiles.  This goes under ~/.config/quicktilecfg.py
'''


profiles = []

basic = {
    'left'           : (
        (0,         0,   0.5,       1),
        (0,         0,   1.0/3,     1),
        (0,         0,   1.0/3 * 2, 1)
    ),
    'middle'         : (
        (0,         0,   1,         1),
        (1.0/3,     0,   1.0/3,     1),
        (1.0/6,     0,   1.0/3 * 2, 1)
    ),
    'right'          : (
        (0.5,       0,   0.5,       1),
        (1.0/3 * 2, 0,   1.0/3,     1),
        (1.0/3,     0,   1.0/3 * 2, 1)
    ),
    'top'            : (
        (0,         0,   1,         0.5),
        (1.0/3,     0,   1.0/3,     0.5)
    ),
    'bottom'         : (
        (0,         0.5, 1,         0.5),
        (1.0/3,     0.5, 1.0/3,     0.5)
    ),
    'top-left'       : (
        (0,         0,   0.5,       0.5),
        (0,         0,   1.0/3,     0.5),
        (0,         0,   1.0/3 * 2, 0.5)
    ),
    'top-right'      : (
        (0.5,       0,   0.5,       0.5),
        (1.0/3 * 2, 0,   1.0/3,     0.5),
        (1.0/3,     0,   1.0/3 * 2, 0.5)
    ),
    'bottom-left'    : (
        (0,         0.5, 0.5,       0.5),
        (0,         0.5, 1.0/3,     0.5),
        (0,         0.5, 1.0/3 * 2, 0.5)
    ),
    'bottom-right'   : (
        (0.5,       0.5, 0.5,       0.5),
        (1.0/3 * 2, 0.5, 1.0/3,     0.5),
        (1.0/3,     0.5, 1.0/3 * 2, 0.5)
    ),
    'maximize'            : 'toggleMaximize',
    'monitor-switch'      : 'cycleMonitors',
    'vertical-maximize'   : ((None,      0,   None,      1),),
    'horizontal-maximize' : ((0,      None,   1,      None),),
    'move-to-center'      : 'moveCenter',
    'cycle-profile'       : 'cycleProfile'
}

chatside = {
    'left'           : (
        (0,         0,   0.5,       1),
        (0,         0,   1.0/3,     1),
        (0,         0,   1.0/3 * 2, 1),
        (0,         0,   1.0/6 , 1)
    ),
    'middle'         : (
        (0,         0,   1,         1),
        (1.0/3,     0,   1.0/3,     1),
        (1.0/6,     0,   5.0/12,    1)
    ),
    'right'          : (
        (0.5,       0,   0.5,       1),
        (1.0/3 * 2, 0,   1.0/3,     1),
        (1.0/3,     0,   1.0/3 * 2, 1),
        (7.0/12,     0,   5.0/12,    1),
        (1.0/6,     0,   5.0/6, 1),
    ),
    'top'            : (
        (0,         0,   1,         0.5),
        (1.0/3,     0,   1.0/3,     0.5)
    ),
    'bottom'         : (
        (0,         0.5, 1,         0.5),
        (1.0/3,     0.5, 1.0/3,     0.5)
    ),
    'top-left'       : (
        (0,         0,   0.5,       0.5),
        (0,         0,   1.0/3,     0.5),
        (0,         0,   1.0/3 * 2, 0.5),
        (0,         0,   1.0/6 , 0.5)
    ),
    'top-right'      : (
        (0.5,       0,   0.5,       0.5),
        (1.0/3 * 2, 0,   1.0/3,     0.5),
        (1.0/3,     0,   1.0/3 * 2, 0.5)
    ),
    'bottom-left'    : (
        (0,         0.5, 0.5,       0.5),
        (0,         0.5, 1.0/3,     0.5),
        (0,         0.5, 2.0/3,     0.5),
        (0,         0.5, 1.0/6,     0.5)
    ),
    'bottom-right'   : (
        (0.5,       0.5, 0.5,       0.5),
        (1.0/3 * 2, 0.5, 1.0/3,     0.5),
        (1.0/3,     0.5, 1.0/3 * 2, 0.5)
    ),
    'maximize'            : 'toggleMaximize',
    'monitor-switch'      : 'cycleMonitors',
    'vertical-maximize'   : ((None,      0,   None,      1),),
    'horizontal-maximize' : ((0,      None,   1,      None),),
    'move-to-center'      : 'moveCenter',
    'cycle-profile'       : 'cycleProfile'
}

keys = {
    'I': 'top-left',
    'O': 'top',
    'P': 'top-right',
    'K': 'left',
    'L': 'middle',
    'semicolon': 'right',
    'comma': 'bottom-left',
    'period': 'bottom',
    'slash': 'bottom-right',
    'apostrophe': 'cycle-profile'
}

general = {
    'ModMask': 'Control Mod4',
    'UseWorkarea': True
}

profiles.append(basic)
profiles.append(chatside)

