import selectable.js
+* (c) 2015 http://www.selectable.js.org
+*/
+(function(e){typeof define=="function"&&define.amd?define(["jquery"],e):e(jQuery)})(function(e){function f(e){return e.replace(/(:|\.|\/)/g,"\\$1")}var t="selectable";e.widget("ui.selectable",e.ui.mouse,{version:"0.0.7",options:{appendTo:"body",autoRefresh:!0,distance:0,filter:"*",tolerance:"touch",selected:null,selecting:null,start:null,stop:null,unselected:null,unselecting:null},_create:function(){var t,n=this;this.element.addClass("ui-selectable"),this.dragged=!1;var r;this.refresh=function(){r=e(n.options.filter,n.element[0]),r.addClass("ui-selectee"),r.each(function(){var t=e(this),r=t.offset();
