import io.sphere.client.shop.model.OrderState;

import javax.annotation.Nonnull;
import javax.annotation.Nullable;
import javax.money.MonetaryAmount;
import java.util.Locale;

/**
 * A payment is the financial transaction of an {@link Order}.
 *
 * <p>To create a payment, you need to use a {@link PaymentService}.
 *
 * <p><b>Warning:</b> Payments are automatically created when an order is created.
 *
 * @see io.sphere.client.shop.payment.PaymentService
 */
public class Payment extends ResourceImpl<PaymentImpl> {
    /** The amount of money that the customer has paid. */
    @Nullable public MonetaryAmount amountPaid;
    /** The amount of money that is still owed. */
    @Nullable public MonetaryAmount amountRemaining;
    /** The amount of money that the customer has authorized. */
    @Nullable public MonetaryAmount authorizedAmount;
    /** The identifier of the external payment service (e.g. PayPal, Adyen
