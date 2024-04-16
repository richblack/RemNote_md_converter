# RemNote_md_converter
RemNote 是一款強大的 Zettelkasten 風格筆記應用程式,可讓使用者將筆記匯出為 Markdown 格式。然而,從 RemNote 匯出筆記時,應用程式會將所有行格式化為列表,這與標準的 Markdown 語法不同。當嘗試使用 Pandoc 等工具將匯出的 Markdown 檔案轉換為其他格式時,此格式化可能會導致問題。

RemNote is a powerful Zettelkasten-style note-taking application that allows users to export their notes in Markdown format. However, when exporting notes from RemNote, the application formats all the lines as lists, which differs from the standard Markdown syntax. This formatting can cause issues when attempting to convert the exported Markdown files into other formats using tools like Pandoc.

為了解決這個問題,RemNote Markdown 轉換器這個計畫提供了一個使用者友善的 Python 應用程式,可將從 RemNote 匯出的 Markdown 檔案無縫轉換為常規的 Markdown 格式。使用此轉換器,使用者可輕鬆將 RemNote 筆記轉換為標準化的 Markdown 結構,確保與各種檔案轉換工具(如 Pandoc)的相容性。

To address this problem, the RemNote Markdown Converter project provides a user-friendly Python application that seamlessly converts the exported RemNote Markdown files into regular Markdown format. By utilizing this converter, users can easily transform their RemNote notes into a standardized Markdown structure, ensuring compatibility with various file conversion tools, such as Pandoc.

使用 RemNote Markdown 轉換器,使用者可以輕鬆彌合 RemNote 獨特的匯出風格與廣泛接受的 Markdown 語法之間的差距。使使用者能夠充分發揮 RemNote 筆記的潛力,啟用平滑轉換為各種檔案格式,提高知識庫的靈活性和可攜性。

With the RemNote Markdown Converter, users can effortlessly bridge the gap between RemNote's unique exporting style and the widely-accepted Markdown syntax. This empowers users to leverage the full potential of their RemNote notes by enabling smooth conversion to a wide range of file formats, enhancing the flexibility and portability of their knowledge base.

無論您需要將 RemNote 筆記轉換為 HTML、PDF 或其他常見的檔案格式,RemNote Markdown 轉換器都可以簡化該過程,節省您的時間和精力。擁抱 RemNote 的 Zettelkasten 筆記力量,並解鎖使用此便利的 Markdown 轉換器,輕鬆跨平台和應用程式共享和重複使用您的筆記的能力。

Whether you need to convert your RemNote notes into HTML, PDF, or other popular file formats, the RemNote Markdown Converter simplifies the process, saving you time and effort. Embrace the power of Zettelkasten note-taking with RemNote, and unlock the ability to effortlessly share and repurpose your notes across different platforms and applications using this convenient Markdown converter.

## 格式標籤 Format Tags
為了自訂轉換過程並實現所需格式,您可以在 RemNote Markdown 檔案中使用特殊標籤。這些標籤為轉換器提供指示,允許您控制輸出格式。只需在相關內容後添加適當的標籤,轉換器將處理相應的格式化。下表總結了可用的標籤及其相應的功能:

To customize the conversion process and achieve desired formatting, you can utilize special tags in your RemNote Markdown files. These tags provide instructions to the converter, allowing you to control the output format. Simply add the appropriate tag after the relevant content, and the converter will handle the formatting accordingly. The following table summarizes the available tags and their corresponding functionality:

| 用法                     | 標籤                       | 處理                                                                                                                                |
|--------------------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Headings 標題            | #h1 ~ #h6                   | MD supports header levels 1 to 6. When converted to Word, they become "Heading 1" to "Heading 6". 支援標題級別 1 到 6。轉換為 Word 時,它們將成為"標題 1"到"標題 6"。 |
| Unordered Lists 無序列表 | #ul                         | List items are preceded by a bullet point, such as a black dot or an asterisk, and are indented one level. Lists can have nested levels, which are further indented. 列表項前面有一個項目符號,如黑點或星號,並縮進一級。列表可以有嵌套級別,進一步縮進。 |
| Ordered Lists 有序列表   | #ol                         | List items are preceded by a marker, such as 1, 2, 3, or a, b, c, and are indented one level. Lists can have nested levels, which are further indented. 列表項前面有一個標記,例如 1、2、3 或 a、b、c,並縮進一級。列表可以有嵌套級別,進一步縮進。 |
| List to Table Conversion 列表到表格轉換 | #ListToTable | ZK software, like RemNote, records tables using indented lists, but when exported, they revert back to indented lists. The converter identifies and converts them back to tables. ZK 軟件(如 RemNote)使用縮進列表記錄表格,但在匯出時,它們會恢復為縮進列表。轉換器可識別並將它們轉換回表格。 |
| Text Alignment 文本對齊  | #centered, #right, #Justified| Word is used daily, but MD does not support these alignment options: center, right, and justified. The converter applies the specified alignment to the text. Word 的文本對齊選項 MD 不支援:居中、右對齊和左右對齊。轉換器將應用指定的對齊方式於文本。|
| Writing Outline 寫作大綱 | #outline                    | Paragraph summary used to remind yourself and AI. It is not displayed in the output and only exists in the ZK software. 段落摘要用於提醒自己和 AI。它不會顯示在輸出中,只存在於 ZK 軟體中。|
| Non-indented Text 非縮進文本| #NoSpace                 | Word's "body" text is indented by default with 2 spaces, NoSpace formats the paragraph in Word with NoSpace style. 本文通常會空兩個字，標示這個標籤表示不要變為一般本文，而是無內縮

在您的 RemNote Markdown 檔案中併入這些標籤,您可以輕鬆控制轉換輸出的格式化,確保您的內容在目標格式中按預期呈現。

By incorporating these tags into your RemNote Markdown files, you can easily control the formatting of the converted output, ensuring that your content is presented as intended in the target format.

## Using
從以下網址下載並解壓可執行檔 Download and extract Executable file from: https://github.com/richblack/RemNote_md_converter/blob/main/md_converter.app.zip

從以下網址下載原始碼 Download source code from: https://github.com/richblack/RemNote_md_converter/blob/main/converter.py
