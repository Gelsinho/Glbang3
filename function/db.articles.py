Ë

    Ê‚ýfv  ã                   ó(   — d dl mZ d„ Zd„ Zd„ Zd„ Zy)é    )ÚMySQLdbc                 óÒ   — d}| j                   j                  t        j                  j                  «      }|j                  |«       |j
                  «       }|j                  «        |S )Nu¸  
        -- Seleciona os campos abaixo
        SELECT art_id, art_title, art_resume, art_thumbnail
        -- desta tabela
        FROM article
        -- art_status Ã© 'on'
        WHERE art_status = 'on'
            -- E art_date Ã© menor ou igual Ã  data atual
            -- NÃ£o obtÃ©m artigos com data futura (agendados)
            AND art_date <= NOW()
        -- Ordena pela data mais recente  
        ORDER BY art_date DESC;
    ©Ú
connectionÚcursorr   ÚcursorsÚ
DictCursorÚexecuteÚfetchallÚclose)ÚmysqlÚsqlÚcurÚarticless       úOC:\Users\andre.ataide\Luferat\Python\jocablog\JocaBlog\functions\db_articles.pyÚget_allr      sP   € ð€Cð ×
Ñ
×
!Ñ
!¤'§/¡/×"<Ñ"<Ó
=€CØ‡KKÔØ|‰|‹~€HØ‡II„Kà€Oó    c                 óÖ   — d}| j                   j                  t        j                  j                  «      }|j                  ||f«       |j
                  «       }|j                  «        |S )Nu  
        SELECT 
            -- Campos do artigo
            art_id, art_date, art_title, art_content,
            -- Campos do autor
            sta_id, sta_name, sta_image, sta_description, sta_type,
            -- Campos especiais
            -- ObtÃ©m a data em PT-BR pelo pseudo-campo `art_datebr`
            DATE_FORMAT(art_date, '%%d/%%m/%%Y Ã s %%H:%%i') AS art_datebr,            
            -- Calcula a idade para `sta_age` considerando ano, mÃªs e dia de nascimento
            TIMESTAMPDIFF(YEAR, sta_birth, CURDATE()) - (DATE_FORMAT(CURDATE(), '%%m%%d') < DATE_FORMAT(sta_birth, '%%m%%d')) AS sta_age
        FROM article
        INNER JOIN staff ON art_author = sta_id
        WHERE art_id = %s
            AND art_status = 'on'
            AND art_date <= NOW();
    )r   r   r   r   r	   r
   Úfetchoner   )r
   Úartidr   r   Úarticles        r   Úget_oner      sT   € ð€Cð" ×
Ñ
×
!Ñ
!¤'§/¡/×"<Ñ"<Ó
=€CØ‡KKeXÔØl‰l‹n€GØ‡II„Kà€Nr   c                 óè   — d}| j                   j                  t        j                  j                  «      }|j                  ||f«       | j                   j
                  «        |j                  «        y)Nz<UPDATE article SET art_view = art_view + 1 WHERE art_id = %sT)r   r   r   r   r	   r
   Úcommitr   )r
   r   r   r   s       r   Úupdate_viewsr   6   sU   € à
H€CØ
×
Ñ
×
!Ñ
!¤'§/¡/×"<Ñ"<Ó
=€CØ‡KKeXÔØ	×Ñ×ÑÔØ‡II„Kàr   c                 óÚ   — d}| j                   j                  t        j                  j                  «      }|j                  ||||f«       |j
                  «       }|j                  «        |S )Nu!  
        -- ObtÃ©m (id, title, thumbnail)
        SELECT art_id, art_title, art_thumbnail
        -- da table `article`
        FROM article
        -- Do author com o id `art_author`
        WHERE art_author = %s
        -- Cujo status Ã© 'on'
            AND art_status = 'on'
            -- Cuja data de publicaÃ§Ã£o estÃ¡ no passado
            AND art_date <= NOW()
            -- NÃ£o obtÃ©m o artigo atual
            AND art_id != %s
        -- Em ordem aleatÃ³ria
        ORDER BY RAND()
        -- AtÃ© 4 artigos
        LIMIT %s;
    r   )r
   Ústaidr   Úlimitr   r   r   s          r   Ú
get_authorr   A   sY   € ð€Cð$ ×
Ñ
×
!Ñ
!¤'§/¡/×"<Ñ"<Ó
=€CØ‡KKe˜U EÐ,Ô-Ø|‰|‹~€HØ‡II„Kà€Or   N)Ú
flask_mysqldbr   r   r   r   r   © r   r   Ú<module>r"      s   ðÝ !òò.ò6ór   