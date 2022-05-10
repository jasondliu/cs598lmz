import select from '../common/select';
import {
  getRepairTaskByRepairTaskId,
  searchRepairTask,
  searchVehicleByLicenseNumber,
  searchVehicleByVin,
  searchVehicleType,
  searchVehicleByLicenseNumberAndVehicleType,
  repairTaskCheck,
  finishRepairTask,
  saveRepairTask,
  saveRepairTaskDetail,
  searchRepairTaskDetail,
  deleteRepairTaskDetailById,
  updateRepairTaskDetail,
  saveRepairPart,
  searchRepairPart,
  deleteRepairPartById,
  updateRepairPart,
} from '../../services/aip';
import RepairTaskSearchForm from './repair-task-search-form';
import RepairTaskForm from './repair-task-form';
import RepairTaskDetailForm from './repair-task-detail-form';
import RepairPartForm from './repair-part-form';
import RepairPartTable from './repair-part-table';
import RepairTaskDetailTable from './repair-task-
