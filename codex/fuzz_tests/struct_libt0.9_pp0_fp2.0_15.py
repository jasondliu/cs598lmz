import _structural.bridge.*;
import _structural.bridge.shape.Shape;
import _structural.bridge.shape.Shape1;
import _structural.bridge.shape.Shape2;
import _structural.bridge.theme.Theme;

class BridgeDemo {
    public static void main(String[] args) {
        final Theme darkTheme = new DarkTheme();
        final Theme lightTheme = new LightTheme();
        final Theme aquaTheme = new AquaTheme();

        final Shape triangle = new Triangle(darkTheme);
        triangle.draw();
        final Shape pentagon = new Pentagon(lightTheme);
        pentagon.draw();
        final Shape hexagon = new Hexagon(aquaTheme);
        hexagon.draw();
    }
}
