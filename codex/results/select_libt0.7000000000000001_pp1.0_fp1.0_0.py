import selection.shapes.Shape;

public class PlaceRectangle extends PlaceShape{
	private Rectangle rectangle;
	
	public PlaceRectangle() {
		super();
		rectangle = new Rectangle();
		shape = rectangle;
		
	}
	
	public void execute() {
		shapesList.add(rectangle);
		rectangle.setX(x);
		rectangle.setY(y);
		rectangle.setHeight(height);
		rectangle.setWidth(width);
		rectangle.setColor(color);
		rectangle.setFillColor(fillColor);
		rectangle.setStrokeColor(strokeColor);
		
		
		
		
		
		//shape.setX(x);
		
	}
	
	
	
	
	

}
