# Python 2.7
# Coded by @HuelderAntunes
# Works on Cinema 4D R18+

import c4d, time
from c4d import utils
from c4d.modules import bodypaint

_SCALE = 0.5 # Default transform scale

def main():
    if(op == None):
        c4d.StatusSetText("Error: Select at least one object.")
        return
		
    c4d.StatusSetText("UVTransform: Processing..")
    c4d.StatusSetSpin()
    c4d.CallCommand(12187)
    c4d.CallCommand(12552)
    tg = op.GetTags()
    ls = tg[len(tg)-1].GetBaseSelect()
    tg[len(tg)-1].Remove()
    lsOn = op.GetPolygonS()
    lsOn.DeselectAll()   
    seila = ls.GetClone()
    ls.DeselectAll()
    c4d.EventAdd()
    c4d.CallCommand(13324)
	
    handle = bodypaint.GetActiveUVSet(doc, c4d.GETACTIVEUVSET_ALL)
    if(handle == None):
        c4d.StatusSetText("Erro: Object without UV Tag.")
        return
		
    uvw = handle.GetUVW()   
    if(uvw == None):
        c4d.StatusSetText("Error: Object with invalid UV Tag.")
        return
		
    settings = c4d.BaseContainer()
    settings[c4d.UVCOMMAND_TRANSFORM_MOVE_X] = 0
    settings[c4d.UVCOMMAND_TRANSFORM_MOVE_Y] = 0
    settings[c4d.UVCOMMAND_TRANSFORM_SCALE_X] = _SCALE
    settings[c4d.UVCOMMAND_TRANSFORM_SCALE_Y] = _SCALE
    settings[c4d.UVCOMMAND_TRANSFORM_ANGLE] = utils.DegToRad(0)
	
    for i in xrange(0,op.GetPolygonCount()):
        if(seila.IsSelected(i)):         
            lsOn.DeselectAll()         
            c4d.CallCommand(13324)
            lsOn.Select(i)
            bodypaint.CallUVCommand(handle.GetPoints(), handle.GetPointCount(), handle.GetPolys(), handle.GetPolyCount(), uvw,
                                    lsOn, handle.GetUVPointSel(), op, handle.GetMode(), c4d.UVCOMMAND_TRANSFORM, settings)
            lsOn.DeselectAll()
			
    handle.SetUVWFromTextureView(uvw, True, True, True)    
    bodypaint.FreeActiveUVSet(handle)
    c4d.CallCommand(13324)
    c4d.StatusClear()
	
if __name__=='__main__':   
    main()
