import io.atlas.medicartcore.domain.Cart;
import io.atlas.medicartcore.domain.CartItem;
import io.atlas.medicartcore.domain.Customer;
import io.atlas.medicartcore.domain.Product;
import io.atlas.medicartcore.dto.ProductDto;
import io.atlas.medicartcore.exception.ResourceNotFoundException;
import io.atlas.medicartcore.repositories.CartItemRepository;
import io.atlas.medicartcore.repositories.CartRepository;
import io.atlas.medicartcore.repositories.CustomerRepository;
import io.atlas.medicartcore.repositories.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

import static java.util.Objects.isNull;

@Service
public class CartService {

    @Aut
