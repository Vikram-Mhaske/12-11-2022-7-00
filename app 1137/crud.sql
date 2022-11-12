-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 11, 2022 at 01:52 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `crud`
--

-- --------------------------------------------------------

--
-- Table structure for table `1`
--

CREATE TABLE `1` (
  `Sr.No` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` int(12) NOT NULL,
  `project` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `clienttable`
--

CREATE TABLE `clienttable` (
  `ID` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` text NOT NULL,
  `phone` text NOT NULL,
  `project` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `clienttable`
--

INSERT INTO `clienttable` (`ID`, `name`, `email`, `phone`, `project`) VALUES
(3, 'vikrm', 'vikrammhaske98@gmailc.om', '09878989898', 'amv'),
(4, 'vikrm', 'vikrammhaske98@gmailc.om', '09878989898', 'asdf'),
(5, 'vikrm', 'vikrammhaske98@gmailc.om', '09878989898', 'asdfasdf asdf');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `status` text NOT NULL,
  `priority` text NOT NULL,
  `d` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`id`, `name`, `email`, `phone`, `status`, `priority`, `d`) VALUES
(26, 'two', 'sadf', 'd', 'completed', 'H', '2022-11-10'),
(27, 'two', 'make new logo', 'd', 'in que', 'M', '2022-11-12'),
(28, 'three', '3', 'c', 'completed', 'L ', '2022-11-03'),
(30, 'one', 'asd@dsf', 'vikram', 'in que', 'H', '2022-11-12'),
(29, 'one', 'asd@dsf', 'vikram', 'in que', 'H', '2022-11-23'),
(25, 'two three', 'make logo', 'muzamil', 'COMPLETED', 'H', '2022-11-11'),
(22, 'samsung', 'make new phone', 'c', 'COMPLETED', 'M', '2022-11-11');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `1`
--
ALTER TABLE `1`
  ADD PRIMARY KEY (`Sr.No`);

--
-- Indexes for table `clienttable`
--
ALTER TABLE `clienttable`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `1`
--
ALTER TABLE `1`
  MODIFY `Sr.No` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `clienttable`
--
ALTER TABLE `clienttable`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
