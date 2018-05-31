# hexo-post
# About
>1. This is a project to post hexo markdwon article through browser.

>2. I have no time to develop more functions now. Will make it better in the future.

>3. If you like it or it helps you,please give me a star.Thanks!

# Install
1. install python3,virtualenv

2. create new virtualenv

      ` virtualenv env`

3. edit the config.py :

      change the `root_path` value to the hexo root folder.
 
4. active the virtual environment and run the command

     ` python hexo-post.py`

# Usage

## 1. preview

![Previes](https://github.com/zc1024/hexo-post/blob/master/demo.png)

## 2. elements explain:
 
 - title: the post article title.It's also the name of the file.If it's Chinese words,it will be convert to pinyin as the file name and article title is still in Chinese.
 
 - tags : the tags for hexo blog. If you have one more tags,please separate it in `,` .
 
 - categories: the categories for hexo blog.If one more,please separate in `,`.

## 3. publish
  When you have accomplished the article editing,you can publish it by click the check icon in the toolbar.
  
# Summary

## 1.Bugs:
   1. Everyone can publish article through this page ,so you should be careful. It will be solved in the future version.
   2. I don't know if it's safe to archive this solution by this way.

# Final

*Welcome to fork it or star it !*

*I wiil appreciate it if you  keep the link of my github project on the html page when  you use it.*
