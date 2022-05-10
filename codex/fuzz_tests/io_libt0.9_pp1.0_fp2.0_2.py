import io.spreadsheet.calculation.api.NumericValue;

import java.util.LinkedList;
import java.util.List;

public class NumericValueImpl implements NumericValue {

    private final List<Double> values;

    private NumericValueImpl(List<Double> values) {
        this.values = new LinkedList<>(values);
    }

    @Override
    public double doubleValue() {
        if (values.size() > 0) {
            return values.get(0);
        } else {
            return 0d;
        }
    }

    @Override
    public int intValue() {
        return (int) doubleValue();
    }

    @Override
    public ValueType 
