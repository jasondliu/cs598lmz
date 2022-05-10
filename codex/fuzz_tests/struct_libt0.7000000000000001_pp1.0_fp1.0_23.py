import _structured_data from './_structured_data';

export default class ProductData extends _structured_data {
	constructor( { data } ) {
		super( 'product', data );
	}

	/**
	 * Product name.
	 * @return {string} Product name.
	 */
	get name() {
		return this.get( 'name' );
	}

	/**
	 * Brand name.
	 * @return {string} Brand name.
	 */
	get brand() {
		return this.get( 'brand' );
	}

	/**
	 * Product description.
	 * @return {string} Product description.
	 */
	get description() {
		return this.get( 'description' );
	}

	/**
	 * Product SKU.
	 * @return {string} SKU.
	 */
	get sku() {
		return this.get( 'sku' );
	}

	/**
	 * Product GTIN.
	 * @return {string} GTIN.
	 */
	get
