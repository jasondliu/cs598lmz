import selectors from './selectors';

import './styles.css';

function CoinExchangeRate() {
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(getRates());
    }, [dispatch]);

    const rates = useSelector(selectors.getRates);
    const loading = useSelector(selectors.getLoading);
    const error = useSelector(selectors.getError);

    return (
        <section className="coin-exchange-rate">
            <h2 className="coin-exchange-rate__header">
                Курс валют
            </h2>

            {loading && (
                <p className="coin-exchange-rate__status">
                    Загрузка...
                </p>
            )}

            {error && (
                <p className="coin-exchange-rate__status">
                    Произошла ошибка
                </p>
            )
