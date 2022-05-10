import selectedToppings from '../selectors/toppings';

const ToppingsList = (props) => (
    <div>
        {
            props.toppings.length === 0 ? (
                <p>No toppings</p>
            ) : (
                props.toppings.map((topping) => {
                    return <Topping key={topping.id} {...topping} />;
                })
            )
        }
    </div>
);

const mapStateToProps = (state) => {
    return {
        toppings: selectedToppings(state.toppings, state.filters)
    };
};

export default connect(mapStateToProps)(ToppingsList);
