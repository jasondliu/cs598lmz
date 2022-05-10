import selectType from '@/components/selectType'
import selectType1 from '@/components/selectType1'
import selectType2 from '@/components/selectType2'
import selectType3 from '@/components/selectType3'
import selectType4 from '@/components/selectType4'
import selectTemplate from '@/components/selectTemplate'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/register',
      name: 'register',
      component: register
    },
    {
      path: '/index',
      name: 'index',
      component: index
    },
    {
      path: '/Index',
      name: 'index',
      component: index
    },
    {
      path: '/shopcart',
      name: 'shopcart',
     
