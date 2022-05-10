import mmapi from '@/api/mmapi'
import Router from 'vue-router'
import { getPIds, getPaths } from '@/utils/auth'
import qs from 'qs'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  base: '/',
  // 路由滚动行为
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { x: 0, y: 0 }
    }
  },
  routes: [
    {
      path: '/',
      name: 'index',
      meta: {
        title: "云管理平台"
      },
      redirect: '/login',
      component: () => import('@/views/index'),
      children: [
        {
          path: 'login',
          name: 'login',
          meta: {
            title: '登录',
            keep
