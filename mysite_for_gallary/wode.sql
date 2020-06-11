-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- 主机： 127.0.0.1
-- 生成日期： 2020-06-09 03:25:47
-- 服务器版本： 10.4.11-MariaDB
-- PHP 版本： 7.2.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `wode`
--

-- --------------------------------------------------------

--
-- 表的结构 `admin`
--

CREATE TABLE `admin` (
  `name` varchar(10) NOT NULL,
  `pwd` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `admin`
--

INSERT INTO `admin` (`name`, `pwd`) VALUES
('admin', '123456');

-- --------------------------------------------------------

--
-- 表的结构 `login`
--

CREATE TABLE `login` (
  `name` varchar(100) NOT NULL,
  `pwd` varchar(100) NOT NULL,
  `dep` varchar(10) NOT NULL,
  `mail` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `login`
--

INSERT INTO `login` (`name`, `pwd`, `dep`, `mail`) VALUES
('', '', '', ''),
('jeremy', 'iamu', 'CST', ''),
('lubenwei', 'niubi', 'APSY', '2231234@163.COM'),
('Marty', 'a123', '', ''),
('nihao', '123456', 'FST', '');

-- --------------------------------------------------------

--
-- 表的结构 `techerlogin`
--

CREATE TABLE `techerlogin` (
  `name` varchar(100) NOT NULL,
  `pwd` varchar(100) NOT NULL,
  `pho` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `techerlogin`
--

INSERT INTO `techerlogin` (`name`, `pwd`, `pho`) VALUES
('1', '1', 1);

--
-- 转储表的索引
--

--
-- 表的索引 `login`
--
ALTER TABLE `login`
  ADD UNIQUE KEY `name` (`name`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
