import mmapi from '../../api/mm';

// Initial state
const state = {
    all: [],
    current_category: false
};

// Getters
const getters = {
    getAll: state => state.all
};

// Actions
const actions = {
    getAll({ commit }) {
        mmapi.getCategories((categories) => {
            commit('setCategories', { list: categories })
        })
    },
};

// Mutations
const mutations = {
    setCategories(state, { list }) {
        state.all = list
    },
    setCurrentCategory(state, { categoryName }) {
        console.log(categoryName)
        state.current_category = categoryName
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}
