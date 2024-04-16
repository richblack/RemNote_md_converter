# RemNote_md_converter
RemNote is a powerful Zettelkasten-style note-taking application that allows users to export their notes in Markdown format. However, when exporting notes from RemNote, the application formats all the lines as lists, which differs from the standard Markdown syntax. This formatting can cause issues when attempting to convert the exported Markdown files into other formats using tools like Pandoc.

To address this problem, the RemNote Markdown Converter project provides a user-friendly Python application that seamlessly converts the exported RemNote Markdown files into regular Markdown format. By utilizing this converter, users can easily transform their RemNote notes into a standardized Markdown structure, ensuring compatibility with various file conversion tools, such as Pandoc.

With the RemNote Markdown Converter, users can effortlessly bridge the gap between RemNote's unique exporting style and the widely-accepted Markdown syntax. This empowers users to leverage the full potential of their RemNote notes by enabling smooth conversion to a wide range of file formats, enhancing the flexibility and portability of their knowledge base.

Whether you need to convert your RemNote notes into HTML, PDF, or other popular file formats, the RemNote Markdown Converter simplifies the process, saving you time and effort. Embrace the power of Zettelkasten note-taking with RemNote, and unlock the ability to effortlessly share and repurpose your notes across different platforms and applications using this convenient Markdown converter.

## Format Tags
To customize the conversion process and achieve desired formatting, you can utilize special tags in your RemNote Markdown files. These tags provide instructions to the converter, allowing you to control the output format. Simply add the appropriate tag after the relevant content, and the converter will handle the formatting accordingly. The following table summarizes the available tags and their corresponding functionality:

| Usage                   | Tag                          | Processing                                                                                                                        |
|-------------------------|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Headings                | #h1 ~ #h6                    | MD supports header levels 1 to 6. When converted to Word, they become "Heading 1" to "Heading 6".                                 |
| Unordered Lists         | #ul                          | List items are preceded by a bullet point, such as a black dot or an asterisk, and are indented one level. Lists can have nested levels, which are further indented. |
| Ordered Lists           | #ol                          | List items are preceded by a marker, such as 1, 2, 3, or a, b, c, and are indented one level. Lists can have nested levels, which are further indented. |
| List to Table Conversion| #ListToTable                 | ZK software, like RemNote, records tables using indented lists, but when exported, they revert back to indented lists. The converter identifies and converts them back to tables. |
| Text Alignment          | #centered, #right, #Justified| Word is used daily, but MD does not support these alignment options: center, right, and justified. The converter applies the specified alignment to the text. |
| Writing Outline         | #outline                     | Paragraph summary used to remind yourself and AI. It is not displayed in the output and only exists in the ZK software.          |
| Non-indented Text       | #NoSpace                     | Word's "body" text is indented by default with 2 spaces, but some text should not be indented, such as table content. Use this tag to prevent indentation. |
| Image Captions          | #ImageCaption                | Word has an image caption format. The converter transforms it into small text below the image and automatically adds numbering.   |
| Table Captions          | #TableCaption                | Word has a table caption format. The converter transforms it into small text above the table and automatically adds numbering.   |

By incorporating these tags into your RemNote Markdown files, you can easily control the formatting of the converted output, ensuring that your content is presented as intended in the target format.

## Install
Download Executable file from: https://github.com/richblack/RemNote_md_converter/blob/main/md_converter.app.zip
Download source code from: https://github.com/richblack/RemNote_md_converter/blob/main/converter.py
