import io.github.mosser.arduinoml.ens.model.Action;
import io.github.mosser.arduinoml.ens.model.Conditional;
import io.github.mosser.arduinoml.ens.model.State;
import io.github.mosser.arduinoml.ens.model.Transition;

import java.util.ArrayList;
import java.util.List;

public class Visitor extends ArduinoMLBaseVisitor<Object> {

    private App theApp;
    private State theState;
    private Transition theTransition;

    @Override
    public Object visitApp(ArduinoMLParser.AppContext ctx) {
        theApp = new App();
        theApp.setName(ctx.ID().toString());
        ctx.type().forEach(type -> type.accept(this));
        ctx.state().forEach(state -> state.accept(this));
        return theApp;
    }

    @Override
    public Object visitType(ArduinoMLParser.TypeContext ctx) {
        Type type
