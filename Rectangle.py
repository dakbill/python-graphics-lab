from graphics import *
win = GraphWin("Rectangle", 300, 300)
rect = Rectangle( Point( 10,10), Point(200, 100 ) )
rect.setFill( "yellow" )
rect.setOutline('black')
rect.setWidth(10)
rect.draw( win )
win.mainloop()
