const dorks = {
    "ログインページ": ['intitle:"login"', 'inurl:admin', 'intitle:"admin login"'],
    "パスワードファイル": ['filetype:log intext:"password"', 'filetype:env "DB_PASSWORD"', 'filetype:conf intext:password'],
    "カメラ/Webカム": ['intitle:"Live View / - AXIS"', 'inurl:"viewerframe?mode="', 'inurl:"webcamxp"'],
    "インデックス公開": ['intitle:"index of" "backup"', 'intitle:"index of" ".git"', 'intitle:"index of" "mp3"'],
    "データベース管理ツール": ['intitle:"phpMyAdmin"', 'intitle:"Mongo Express"', 'intitle:"Adminer"'],
    "エラー/脆弱性情報": ['intext:"You have an error in your SQL syntax"', 'intext:"Warning: mysql_fetch_array()"', 'intext:"Fatal error"']
  };

  const categorySelect = document.getElementById("categorySelect");
  const templateSelect = document.getElementById("templateSelect");
  const resultBox = document.getElementById("resultBox");

  // カテゴリをセット
  for (const key in dorks) {
    const option = document.createElement("option");
    option.value = key;
    option.textContent = key;
    categorySelect.appendChild(option);
  }

  // カテゴリ変更時、テンプレート更新
  categorySelect.addEventListener("change", () => {
    const selected = categorySelect.value;
    templateSelect.innerHTML = "";
    dorks[selected].forEach(d => {
      const option = document.createElement("option");
      option.value = d;
      option.textContent = d;
      templateSelect.appendChild(option);
    });
  });

  // 初期選択
  categorySelect.dispatchEvent(new Event("change"));

  function useTemplate() {
    const dork = templateSelect.value;
    resultBox.textContent = dork;
  }

  function generateCustomDork() {
    const keywords = document.getElementById("keywordsInput").value.split(",").map(k => k.trim());
    const field = document.getElementById("fieldSelect").value;
    const logic = document.getElementById("logicSelect").value;

    const parts = keywords.map(word => {
      return field === "text" ? `"${word}"` : `${field}:"${word}"`;
    });

    const dork = parts.join(` ${logic} `);
    resultBox.textContent = dork;
  }

  function searchGoogle() {
    const query = resultBox.textContent;
    if (query) {
      window.open("https://www.google.com/search?q=" + encodeURIComponent(query), "_blank");
    }
  }