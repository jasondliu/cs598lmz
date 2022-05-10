import selectors from '../selectors/selectors'

const initialState = {
    user: {
        isAuthenticated: false,
        user: null,
        error: null,
        isLoaded: false
    }
}

export default function user(state = initialState, action) {
    switch (action.type) {
        case types.USER_LOGIN_REQUEST:
            return {
                ...state,
                user: {
                    ...state.user,
                    error: null
                }
            }
        case types.USER_LOGIN_SUCCESS:
            return {
                ...state,
                user: {
                    isLoaded: true,
                    isAuthenticated: true,
                    user: action.payload,
                    error: null
                }
            }
        case types.USER_LOGIN_FAILURE:
            return {
                ...state,
                user: {
                    isLoaded: true,
                    isAuthenticated: false,
                    user: null,
                    error: action.payload
                }
            }
        case types
