// ==UserScript==
// @name         fanbox Download
// @namespace    https://scripts.zombie110year.top
// @version      0.1
// @description  下载 fanbox 投稿页面中的图片文件, 按 {二级域名}.fanbox.cc_posts_{数字ID}_{序列数}.{图片后缀名} 保存
// @author       zombie110year
// @match        https://*.fanbox.cc/posts/*
// @icon         https://www.google.com/s2/favicons?domain=fanbox.cc
// @grant        GM_setClipboard
// ==/UserScript==

(function() {
    'use strict';
    let a = document.createElement("button");
    a.innerText = "下载";
    a.addEventListener("click", trigger);
    setTimeout(() => {
        let menu = document.querySelector("#root > div.sc-1spzamr-1.hMDhRk > div.sc-1spzamr-2.eYvyvJ > div:nth-child(2) > div.sc-38wvbn-0.gYeWrH > div > div.sc-rd992x-1.injOTk > div > div.sc-1vjtieq-2.ljzktz > div");
        menu.appendChild(a);
    }, 3000);
})();

function buildDownloadInfo() {
    'use strict';
    const filename_prefix = `${location.hostname}${location.pathname.replaceAll("/", "_")}_`;
    const links = [...document.querySelectorAll("#root article > div > div > div > div > div > div > a")].map(
        (a) => a.getAttribute("href"));
    let download_info = {
        "links": links,
        "origin": location.origin,
        "href": location.href,
        "user_agent": navigator.userAgent,
    };
    return download_info;
}


function trigger() {
    'use strict';
    console.debug("[fanbox Download] downloading...");
    const download_info = buildDownloadInfo();
    console.debug(`[fanbox Download] ${download_info.size} pictures founded`);
    const json_info = JSON.stringify(download_info);
    GM_setClipboard(json_info, "text");
    console.log(json_info);
    alert("下载信息复制到剪贴板");
}
