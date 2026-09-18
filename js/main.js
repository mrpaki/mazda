/* EAST Auto Servis — main.js */
(function () {
  "use strict";

  /* Header: senka na skrol */
  var header = document.querySelector(".site-header");
  var onScroll = function () { header.classList.toggle("is-scrolled", window.scrollY > 8); };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* Mobilni meni */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(open));
      toggle.setAttribute("aria-label", open ? "Zatvori meni" : "Otvori meni");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("is-open")) {
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.focus();
      }
    });
  }

  /* Hero video: poster ostaje ako video ne postoji ili korisnik ne želi animacije */
  var video = document.querySelector(".hero-media");
  if (video) {
    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var tach = document.querySelector(".tach");
    var fill = tach && tach.querySelector(".tach-fill");
    var sound = document.querySelector(".hero-sound");
    var drop = function () {
      video.remove();
      if (tach) tach.classList.remove("tach--live");
      if (sound) sound.remove();
    };
    if (reduce) { video.removeAttribute("autoplay"); video.pause(); }
    /* Sa više <source>, poslednji (mp4) koji zakaže znači da su svi pali → poster */
    var sources = video.querySelectorAll("source");
    if (sources.length) sources[sources.length - 1].addEventListener("error", drop);
    video.addEventListener("error", drop);

    /* Obrtomer prati obrtaje motora iz snimljenog envelope-a (js/hero-rev.js) */
    var data = window.HERO_REV;
    if (fill && data && data.rev && data.rev.length && !reduce) {
      var rev = data.rev, fps = data.fps || 30, N = rev.length, live = false;
      var loop = function () {
        var i = Math.floor(video.currentTime * fps) % N;
        fill.style.width = rev[i] + "%";
        requestAnimationFrame(loop);
      };
      var start = function () {
        if (live) return;
        live = true;
        tach.classList.add("tach--live");
        loop();
      };
      video.addEventListener("playing", start);
      if (!video.paused && video.readyState >= 2) start();
    }

    /* Dugme za zvuk motora */
    if (sound) {
      if (reduce) {
        sound.remove();
      } else {
        sound.addEventListener("click", function () {
          video.muted = !video.muted;
          var on = !video.muted;
          if (on) { var p = video.play(); if (p && p.catch) p.catch(function () {}); }
          sound.classList.toggle("is-on", on);
          sound.setAttribute("aria-pressed", String(on));
          sound.setAttribute("aria-label", on ? "Isključi zvuk motora" : "Uključi zvuk motora");
          var txt = sound.querySelector(".hero-sound-txt");
          if (txt) txt.textContent = on ? "Zvuk uključen" : "Zvuk";
        });
      }
    }
  }

  /* Filter galerije */
  var filterBar = document.querySelector(".filters");
  if (filterBar) {
    var items = document.querySelectorAll("[data-cat]");
    var count = document.querySelector(".count");
    var setCount = function (n) { if (count) count.textContent = n + (n === 1 ? " fotografija" : (n % 10 >= 2 && n % 10 <= 4 && (n < 10 || n > 20) ? " fotografije" : " fotografija")); };
    setCount(items.length);
    filterBar.addEventListener("click", function (e) {
      var btn = e.target.closest("button");
      if (!btn) return;
      var f = btn.dataset.filter;
      filterBar.querySelectorAll("button").forEach(function (b) { b.setAttribute("aria-pressed", String(b === btn)); });
      var n = 0;
      items.forEach(function (el) {
        var show = f === "sve" || el.dataset.cat === f;
        el.hidden = !show;
        if (show) n++;
      });
      setCount(n);
    });
  }

  /* Lightbox */
  var lb = document.getElementById("lightbox");
  if (lb && typeof lb.showModal === "function") {
    var img = lb.querySelector(".lb-stage img");
    var cap = lb.querySelector(".lb-caption");
    var pos = lb.querySelector(".lb-pos");
    var list = [], idx = 0, opener = null;

    var render = function () {
      var a = list[idx];
      img.src = a.getAttribute("href");
      img.alt = a.dataset.caption || "";
      cap.textContent = a.dataset.caption || "";
      pos.textContent = (idx + 1) + " / " + list.length;
    };
    var go = function (d) { idx = (idx + d + list.length) % list.length; render(); };

    document.addEventListener("click", function (e) {
      var a = e.target.closest("a[data-lb]");
      if (!a) return;
      e.preventDefault();
      opener = a;
      list = Array.prototype.filter.call(
        document.querySelectorAll('a[data-lb="' + a.dataset.lb + '"]'),
        function (el) { return !el.hidden; }
      );
      idx = list.indexOf(a);
      render();
      lb.showModal();
    });
    lb.querySelector(".lb-prev").addEventListener("click", function () { go(-1); });
    lb.querySelector(".lb-next").addEventListener("click", function () { go(1); });
    lb.querySelector(".lb-close").addEventListener("click", function () { lb.close(); });
    lb.addEventListener("keydown", function (e) {
      if (e.key === "ArrowLeft") go(-1);
      if (e.key === "ArrowRight") go(1);
    });
    lb.addEventListener("click", function (e) { if (e.target === lb || e.target.classList.contains("lb-stage")) lb.close(); });
    lb.addEventListener("close", function () { img.removeAttribute("src"); if (opener) opener.focus(); });
  }

  /* Forma za zakazivanje — otvara mejl klijent sa popunjenom porukom.
     Za slanje sa servera zameniti ovaj deo (npr. Formspree ili PHP mail). */
  var form = document.getElementById("booking");
  if (form) {
    var status = form.querySelector(".form-status");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var required = form.querySelectorAll("[required]");
      var firstBad = null;
      required.forEach(function (el) {
        var bad = !el.value.trim();
        el.setAttribute("aria-invalid", String(bad));
        if (bad && !firstBad) firstBad = el;
      });
      if (firstBad) {
        status.textContent = "Upišite ime i broj telefona da bismo mogli da vas pozovemo.";
        status.classList.add("is-error");
        firstBad.focus();
        return;
      }
      status.classList.remove("is-error");
      var v = function (id) { var el = form.querySelector("#" + id); return el ? el.value.trim() : ""; };
      var body = [
        "Ime: " + v("ime"),
        "Telefon: " + v("telefon"),
        "Model i godište: " + v("model"),
        "Usluga: " + v("usluga"),
        "Željeni termin: " + v("termin"),
        "",
        v("poruka")
      ].join("\n");
      var subject = "Zakazivanje servisa: " + (v("model") || v("ime"));
      window.location.href = "mailto:office@eastservis.rs?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
      status.textContent = "Otvorili smo vaš mejl program sa popunjenom porukom. Pošaljite je i javićemo vam se sa terminom.";
    });
  }

  /* Potpis izrade: klik na auto → auto odlazi, ostaje tekst sa linkom */
  var credit = document.querySelector(".credit");
  if (credit) {
    var car = credit.querySelector(".credit-car");
    car.addEventListener("click", function () {
      credit.classList.add("is-open");
      car.setAttribute("aria-expanded", "true");
      var link = credit.querySelector(".credit-text a");
      setTimeout(function () {
        car.hidden = true;
        if (link) link.focus({ preventScroll: true });
      }, 1300);
    });
  }

  /* Godina u footeru */
  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
})();
