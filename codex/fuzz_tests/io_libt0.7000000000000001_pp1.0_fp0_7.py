import io.pivotal.bds.gemfirexd.util.TransactionId;

@Region("Transaction")
@SuppressWarnings("serial")
public class Transaction extends BaseEntity<TransactionKey> {

    private int securityId;
    private int quantity;
    private BigDecimal price;
    private TransactionType transactionType;
    private int status;

    public Transaction() {
    }

    public Transaction(TransactionId xid, int securityId, int quantity, BigDecimal price, String status) {
        super(new TransactionKey(xid));
        this.securityId = securityId;
        this.quantity = quantity;
        this.price = price;
        this.status = Integer.parseInt(status);
    }

    public int getSecurityId() {
        return securityId;
    }

    public void setSecurityId(int securityId) {
        this.securityId = securityId;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

   
