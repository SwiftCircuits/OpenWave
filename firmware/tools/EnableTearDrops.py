import pcbnew

board = pcbnew.GetBoard()

for module in board.GetFootprints():
    for pad in module.Pads():
        # Directly clear the "do not create teardrop" flag.
        pad.m_bDoNotCreateTeardrop = False

pcbnew.Refresh()
