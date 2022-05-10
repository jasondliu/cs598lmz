import selectedProducts, {
    findProduct,
    findProducts,
    addProduct,
    updateProduct,
    deleteProduct,
} from './reducer';
import {
    SelectedProductFixture,
    SelectedProductFixtureTwo,
    SelectedProductNoIdFixture,
} from './fixtures';
import { ProductFixture } from '../../../fixtures';

describe('selectedProducts reducer', () => {
    let state;
    beforeEach(() => {
        state = selectedProducts(undefined, {
            type: '',
        });
    });

    describe('findProduct', () => {
        it('should return null if no Product is selected', () => {
            expect(findProduct(state)).toEqual(null);
        });

        it('should return the selected Product', () => {
            const product = ProductFixture;
            state = { selectedProducts: { currentSelectedProductId: product.id, data: {} } };
            state = updateProduct(state, product);

            expect(findProduct(state)).toEqual(ProductFixture);
       
