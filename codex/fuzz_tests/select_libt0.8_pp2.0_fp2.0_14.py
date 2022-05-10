import selector from './selector'

function mapStateToProps(state, { params: { productId } }) {
  return {
    product: selector(state, productId)
  }
}

function mapDispatchToProps() {
  return {
    saveProduct: () => {
      console.log('Save product')
    }
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(ProductDetail)
