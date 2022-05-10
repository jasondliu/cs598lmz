import selectedList from './selectedList.js'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    selectedList,
    cartList
  }
})
