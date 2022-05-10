import io.github.mthli.knife.util.UnicodeUtils;

public class MQuoteSpan extends CharacterStyle implements UpdateAppearance {
    private int color;
    private final float stripeWidth;
    private final float gapWidth;

    public MQuoteSpan() {
        super();
        this.stripeWidth = 2;
        this.gapWidth = 2;
        this.color = 0;
    }

    public MQuoteSpan(int color) {
        super();
        this.stripeWidth = 2;
        this.gapWidth = 2;
        this.color = color;
    }

    public int getColor() {
        return color;
    }

    public void setColor(int color) {
        this.color = color;
    }

    @Override
    public void updateDrawState(TextPaint textPaint) {
        textPaint.setColor(color);
    }

    @Override
    public void drawLeadingMargin(
            Canvas canvas,
            Paint paint,
            int x,
            int dir,
            int top,
