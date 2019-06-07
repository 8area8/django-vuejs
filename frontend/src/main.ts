import Vue from "vue";
import "./plugins/axios";
import "./plugins/vuetify";
import App from "./App.vue";
import router from "./router";
import store from "./store";

Vue.config.productionTip = false;

Vue.config.devtools = process.env.NODE_ENV === "development";
const app = new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
(window as any).__VUE_DEVTOOLS_GLOBAL_HOOK__.Vue = app.constructor;
