-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 23, 2023 at 07:26 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `image_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `translations`
--

CREATE TABLE `translations` (
  `id` int(11) NOT NULL,
  `language` varchar(255) DEFAULT NULL,
  `photos` varchar(255) DEFAULT NULL,
  `original_text` varchar(255) DEFAULT NULL,
  `translated_text` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `translations`
--

INSERT INTO `translations` (`id`, `language`, `photos`, `original_text`, `translated_text`) VALUES
(31, 'hi', 'sample_images/4._sample.jpg', 'I , Suresh Padala , here by declare that all the information Submitted by me in the application form is correct , true and valid . I will present the Supporting documents as and when required .', 'मैं, सुरेश पडाला, यहाँ यह घोषणा करते हैं कि आवेदन पत्र में मेरे द्वारा प्रस्तुत सभी जानकारी सही, सही और मान्य है।मैं आवश्यक होने पर सहायक दस्तावेजों को प्रस्तुत करूंगा।'),
(32, 'gu', 'sample_images/4._sample.jpg', 'I , Suresh Padala , here by declare that all the information Submitted by me in the application form is correct , true and valid . I will present the Supporting documents as and when required .', 'હું, સુરેશ પાદલા, અહીં ઘોષણા કરીને કે અરજી ફોર્મમાં મારા દ્વારા સબમિટ કરેલી બધી માહિતી સાચી, સાચી અને માન્ય છે.હું જ્યારે જરૂરી હોય ત્યારે સહાયક દસ્તાવેજો રજૂ કરીશ.'),
(33, 'en', 'sample_images/6. sample.png', 'सभी मनुष्यों को गौरव और अधिकारों के मामले में जन्मजात स्वतन्त्रता और समानता प्राप्त है । उन्हें बुद्धि और अन्तरात्मा की देन प्राप्त है और परस्पर उन्हें भाईचारे के भाव से बर्ताव करना चाहिए ।', 'All humans have congenital freedom and equality in terms of pride and rights.They have the gift of intelligence and conscience and they should treat them with a sense of brotherhood.'),
(34, 'gu', 'sample_images/6. sample.png', 'सभी मनुष्यों को गौरव और अधिकारों के मामले में जन्मजात स्वतन्त्रता और समानता प्राप्त है । उन्हें बुद्धि और अन्तरात्मा की देन प्राप्त है और परस्पर उन्हें भाईचारे के भाव से बर्ताव करना चाहिए ।', 'બધા માણસોમાં ગૌરવ અને અધિકારોની દ્રષ્ટિએ જન્મજાત સ્વતંત્રતા અને સમાનતા હોય છે.તેમની પાસે બુદ્ધિ અને અંત conscience કરણની ભેટ છે અને તેઓએ તેમની સાથે ભાઈચારોની ભાવનાથી વર્તવું જોઈએ.'),
(35, 'en', 'sample_images/7. sample.jpg', 'ਮਹਿਲਾ ਅਤੇ ਅਖਿਲ ਦੀ ਸੀ ਬੂਟਿਆਂ , ਵੇ ਧੀ ਮਯ , ਅਮਲੀ , ਅਬਰਕ , ਮਕ ਨਾਮ ਲੀਗਲ ਰੈਸਮੀ ਕਿਰਦਾਰ ਕੇ ਅਗਲ હોય છે અને તેની પર બંધુત્વની ભાવનાથી વવું જોઈએ .', 'Women\'s c boards and Akhil\'s c boards, practical, abstinations, yes, the name Legal Received aorta'),
(36, 'hi', 'sample_images/7. sample.jpg', 'ਮਹਿਲਾ ਅਤੇ ਅਖਿਲ ਦੀ ਸੀ ਬੂਟਿਆਂ , ਵੇ ਧੀ ਮਯ , ਅਮਲੀ , ਅਬਰਕ , ਮਕ ਨਾਮ ਲੀਗਲ ਰੈਸਮੀ ਕਿਰਦਾਰ ਕੇ ਅਗਲ હોય છે અને તેની પર બંધુત્વની ભાવનાથી વવું જોઈએ .', 'महिला सी बोर्ड और अखिल के सी बोर्ड, व्यावहारिक, संयोजन, हाँ, नाम कानूनी महाधमनी प्राप्त हुआ');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `translations`
--
ALTER TABLE `translations`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `translations`
--
ALTER TABLE `translations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
