import select from 'select-dom';
+
+export default function init() {
+	const combo = select('.js-user-profile-nav-container .mb-2 .dropdown-menu .dl-horizontal .text-muted')[1].innerText;
+	const daily = select('.js-user-profile-nav-container .mb-2 .dropdown-menu .dl-horizontal .text-muted')[3].innerText;
+
+	const container = select('.js-user-profile-nav-container')[1];
+	const div = document.createElement('div');
+	div.className = "dropdown-menu mb-2";
+
+	const dl = document.createElement('dl');
+	dl.className = "dl-horizontal";
+
+	const dt = document.createElement('dt');
+	dt.innerText = "Combos";
+
+	const dd = document.createElement('dd');
+	dd.innerText = combo;
+	dd.className = "text-muted
