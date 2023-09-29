--  Have no way to create a M View on MARIADB, but, you can create a table from a select, doing this separation.

use base;
CREATE Table `mvw_en.transliteration` AS
Select * FROM TB_quran Where edition = 'en.transliteration';

CREATE Table `mvw_en.ahmedali` AS
Select * FROM TB_quran Where edition = 'en.ahmedali';