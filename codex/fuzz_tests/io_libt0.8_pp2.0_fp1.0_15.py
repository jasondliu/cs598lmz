import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Api(tags = {"Receipt"}, description = "Receipt Management")
@RestController
@RequestMapping("receipt")
public class ReceiptController {

    @Autowired
    private ReceiptService receiptService;

    @ApiOperation(value = "Receipt creation", response = Receipt.class)
    @PostMapping
    public Receipt create(@RequestBody Receipt receipt) {
        return receiptService.create
